import os
import sys

import pandas as pd
import streamlit as st

from solution_accelerator.core.orchestrator import run_pipeline

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# -------------------------------
# HELPERS
# -------------------------------


def render_back_button():
    if st.session_state.step > 1:
        if st.button("⬅ Back"):
            st.session_state.step -= 1
            st.rerun()


# -------------------------------
# CONFIG
# -------------------------------

WIZARD_CONFIG = {
    "Pipes": {
        "dimensions": ["1 inch", "2 inch", "4 inch", "6 inch"],
        "materials": ["SS316L", "Carbon Steel", "Alloy Steel"],
        "specs": ["ASTM A312", "ASTM A106", "API 5L"],
    },
    "Pumps": {
        "dimensions": ["1 HP", "5 HP", "10 HP"],
        "materials": ["Cast Iron", "Stainless Steel"],
        "specs": ["ISO 2858", "API 610"],
    },
    "Valves": {
        "dimensions": ["1 inch", "2 inch", "6 inch"],
        "materials": ["Brass", "Steel", "SS"],
        "specs": ["API 600", "API 602"],
    },
    "Cables": {
        "dimensions": ["1 sqmm", "2.5 sqmm", "10 sqmm"],
        "materials": ["Copper", "Aluminium"],
        "specs": ["IS 694", "IEC 60502"],
    },
}


# -------------------------------
# RESET BUTTON
# -------------------------------

if st.button("🔄 Start New Requirement"):
    for key in ["started", "result", "step", "requirement"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()


# -------------------------------
# HEADER
# -------------------------------

st.title("🤖 AI Procurement Copilot")

role = st.selectbox("Select Role", ["Indentor", "Procurement Manager"])
st.caption("End-to-End Procurement Intelligence Workflow")

st.markdown("---")


# -------------------------------
# ROLE-SPECIFIC INPUT
# -------------------------------

if role == "Procurement Manager":
    st.subheader("🧾 Requirement Input")
    user_input = st.text_input("Enter your requirement")
else:
    user_input = None


# -------------------------------
# SESSION STATE INIT
# -------------------------------

if "started" not in st.session_state:
    st.session_state.started = False

if "result" not in st.session_state:
    st.session_state.result = None


# -------------------------------
# RUN BUTTON LOGIC
# -------------------------------

if role == "Procurement Manager":
    if st.button("Run"):
        st.session_state.result = run_pipeline(user_input)
        st.session_state.started = True
        st.rerun()

elif role == "Indentor":
    st.session_state.started = True


# -------------------------------
# MAIN APP
# -------------------------------

if st.session_state.started:
    # =========================================
    # 🔥 INDENTOR FLOW
    # =========================================

    if role == "Indentor":
        st.subheader("🧾 Requirement Builder")

        if "step" not in st.session_state:
            st.session_state.step = 1
            st.session_state.requirement = {}

        total_steps = 5
        current_step = min(st.session_state.step, total_steps)
        st.progress(current_step / total_steps)
        st.caption(f"Step {current_step} of {total_steps}")

        # -------- STEP 1 --------
        if st.session_state.step == 1:
            category = st.selectbox(
                "What type of material do you require?",
                list(WIZARD_CONFIG.keys()),
            )

            if st.button("Next"):
                st.session_state.requirement["category"] = category
                st.session_state.step = 2
                st.rerun()

        # -------- STEP 2 --------
        elif st.session_state.step == 2:
            render_back_button()

            qty = st.number_input("Enter Quantity", min_value=1)

            if st.button("Next"):
                st.session_state.requirement["quantity"] = qty
                st.session_state.step = 3
                st.rerun()

        # -------- STEP 3 --------
        elif st.session_state.step == 3:
            render_back_button()

            category = st.session_state.requirement["category"]

            dimension = st.selectbox(
                "Select Dimensions",
                WIZARD_CONFIG[category]["dimensions"],
            )

            if st.button("Next"):
                st.session_state.requirement["dimension"] = dimension
                st.session_state.step = 4
                st.rerun()

        # -------- STEP 4 --------
        elif st.session_state.step == 4:
            render_back_button()

            category = st.session_state.requirement["category"]

            material = st.selectbox(
                "Select Material",
                WIZARD_CONFIG[category]["materials"],
            )

            if st.button("Next"):
                st.session_state.requirement["material"] = material
                st.session_state.step = 5
                st.rerun()

        # -------- STEP 5 --------
        elif st.session_state.step == 5:
            render_back_button()

            category = st.session_state.requirement["category"]

            spec = st.selectbox(
                "Select Specification",
                WIZARD_CONFIG[category]["specs"],
            )

            if st.button("Submit"):
                st.session_state.requirement["spec"] = spec
                st.session_state.step = 6
                st.rerun()

        # -------- FINAL --------
        elif st.session_state.step == 6:
            req = st.session_state.requirement

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Category", req.get("category"))
                st.metric("Material", req.get("material"))

            with col2:
                st.metric("Quantity", req.get("quantity"))
                st.metric("Dimension", req.get("dimension"))

            with col3:
                st.metric("Specification", req.get("spec"))

            # Category intelligence
            cat = req.get("category", "").lower()

            if cat == "pipes":
                st.info(
                    "🧵 Pipe procurement emphasizes pressure rating & corrosion resistance"
                )
            elif cat == "pumps":
                st.info("⚙️ Pump procurement emphasizes efficiency & reliability")
            elif cat == "cables":
                st.info("🔌 Cable procurement emphasizes insulation & load capacity")
            elif cat == "valves":
                st.info("🔩 Valve procurement emphasizes sealing & pressure class")

            # Run pipeline
            result = run_pipeline(str(req))

            st.subheader("🚢 Shipment Tracking")

            shipping = result.get("shipping", {})

            if shipping and "error" not in shipping:
                st.write(f"Vessel: {shipping.get('vessel_name')}")
                st.write(f"Status: {shipping.get('status')}")
            else:
                st.warning("Tracking unavailable")

        st.stop()

    # =========================================
    # 🔥 PROCUREMENT MANAGER FLOW
    # =========================================

    elif role == "Procurement Manager":
        if not st.session_state.result:
            st.warning("Please enter a requirement first and click Run.")
            st.stop()

        result = st.session_state.result
        parsed = result["parsed_request"]

        category = parsed.get("category", "Unknown")

        # ---------------- SUMMARY ----------------
        st.markdown(f"""
        ### 📦 Requirement Summary
        **Category:** {category}
        **Material:** {parsed.get("material", "-")}
        """)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Category", parsed.get("category", "-"))
        with col2:
            st.metric("Material", parsed.get("material", "-"))
        with col3:
            st.metric("Quantity", parsed.get("quantity", "-"))

        st.markdown("---")

        # ---------------- VENDORS + PRICE ----------------
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f"🏭 Top Vendors for {category}")
            st.info("Score = 0.5 × Price + 0.3 × Delivery + 0.2 × Reliability")
            for e in result["ranked_entities"]:
                st.write(f"**{e['name']}** — Score: {e['score']}")

        with col2:
            st.subheader("💰 Price Insights")
            st.json(result["price_range"])

        st.markdown("---")

        # ---------------- VENDOR INSIGHTS ----------------
        st.subheader("⚠️ Vendor Insights")

        for insight in result.get("entity_insights", []):
            flags = ", ".join(insight["flags"]) if insight["flags"] else "No risks"
            st.write(f"**{insight['name']}** → {flags}")

        st.markdown("---")

        # ---------------- MARKET INTELLIGENCE ----------------
        st.subheader("📈 Live Market Intelligence")

        market_data = result.get("market_data", {})

        cols = st.columns(3)

        for i, (name, series) in enumerate(market_data.items()):
            if series is None or len(series) < 2:
                continue

            latest = series.iloc[-1]
            prev = series.iloc[-2]
            pct = ((latest - prev) / prev) * 100

            with cols[i]:
                st.metric(
                    label=name,
                    value=f"${round(latest, 2)}",
                    delta=f"{round(pct, 2)}%",
                )

        for name, series in market_data.items():
            if series is not None:
                df = pd.DataFrame(series)
                df.columns = ["Price"]
                st.line_chart(df)

        st.markdown("---")

        # ---------------- RFQ ----------------
        st.subheader(f"📧 RFQ Draft for {category}")
        st.text_area("Generated RFQ", result["rfq_email"], height=200)

        st.markdown("---")

        # ---------------- QUOTE COMPARISON ----------------
        st.subheader(f"📊 Quote Comparison for {category}")

        for q in result["quote_comparison"]:
            st.markdown(f"""
            **{q["entity"]}**

            - Price: ₹{q["price"]}
            - Delivery: {q["delivery"]} days
            - Score: {q["score"]}
            """)

            if q["missing_items"]:
                st.warning(f"Missing: {', '.join(q['missing_items'])}")

        best = max(result["quote_comparison"], key=lambda x: x["score"])

        st.success(f"""
        ✅ Recommended Vendor: **{best["entity"]}**
        Score: {best["score"]}
        Reason: Best balance of price, delivery, and completeness
        """)

        st.markdown("---")

        # ---------------- SHIPPING ----------------
        st.subheader("🚢 Shipping Tracking")

        shipping = result.get("shipping", {})

        if shipping and "error" not in shipping:
            coords = shipping.get("coordinates", {})
            st.map(pd.DataFrame([{"lat": coords.get("lat"), "lon": coords.get("lon")}]))
        else:
            st.warning("Tracking unavailable")

        st.markdown("---")

        # ---------------- RECONCILIATION ----------------
        st.subheader("💳 Invoice Reconciliation")

        rec = result["reconciliation"]

        st.write("PO:", rec["po"])
        st.write("GRN:", rec["grn"])
        st.write("Invoice:", rec["invoice"])

        if rec["issues"]:
            for issue in rec["issues"]:
                st.error(issue)
        else:
            st.success("All matched")
