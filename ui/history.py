import streamlit as st


def render_history(
    orders
):

    with st.popover(
        f"📜 History ({len(orders)})"
    ):

        st.subheader(
            "Riwayat Order"
        )

        if not orders:

            st.info(
                "Belum ada riwayat order."
            )

            return

        for order in orders:

            order_id = order[0]

            total = order[1]

            status = order[2]

            if status.lower() == "paid":

                badge = "🟢"

            elif status.lower() == "unpaid":

                badge = "🟡"

            else:

                badge = "🔴"

            with st.container():

                st.markdown(
                    f"### {badge} Order #{order_id}"
                )

                st.write(
                    f"💰 Rp{total:,}"
                )

                st.write(
                    f"Status : **{status.upper()}**"
                )

                st.divider()