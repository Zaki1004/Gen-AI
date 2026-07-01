import streamlit as st

from services.order_service import (
    checkout
)

from services.payment_service import (
    get_order,
    pay_order
)

from services.cart_session_service import (
    clear_cart
)


def render_cart(
    cart,
    total
):

    with st.popover(
        f"🛒 Cart ({len(cart)})"
    ):

        # ==========================
        # CART
        # ==========================

        if cart:

            st.subheader("🛒 Keranjang")

            st.caption(
                "Berikut pesanan yang akan Anda checkout."
            )

            for item in cart:

                st.markdown(
                    f"""
**☕ {item['name']}**

Jumlah : **{item['quantity']}**

Subtotal : **Rp{item['price'] * item['quantity']:,}**

---
"""
                )

            st.metric(
                "💰 Total",
                f"Rp{total:,}"
            )

            if st.button(
                "Checkout",
                use_container_width=True,
                key="checkout_button"
            ):

                result = checkout(
                    cart,
                    total
                )

                st.session_state.payment_token = (
                    result["payment_token"]
                )

                st.success(
                    "🎉 Checkout berhasil dibuat!"
                )

                st.caption(
                    "Silakan lanjutkan ke proses pembayaran."
                )

                st.rerun()

        else:

            st.markdown("## 🛒")

            st.caption(
                "Keranjang Anda masih kosong."
            )

            st.info(
                "Tambahkan menu favorit melalui chat."
            )

        # ==========================
        # PAYMENT
        # ==========================

        if "payment_token" not in st.session_state:

            return

        token = st.session_state.payment_token

        order = get_order(
            token
        )

        if not order:

            return

        st.divider()

        st.subheader(
            "💳 Pembayaran"
        )

        order_id = order[0]
        status = order[1]
        total_price = order[2]

        st.write(
            f"**Order ID :** {order_id}"
        )

        st.metric(
            "💰 Total Pembayaran",
            f"Rp{total_price:,}"
        )

        if status == "paid":

            st.success(
                "🟢 Pembayaran selesai"
            )

            st.caption(
                "Terima kasih telah memesan di CoffeeBot ☕"
            )

        else:

            st.warning(
                "🟡 Menunggu pembayaran"
            )

            st.caption(
                "Selesaikan pembayaran untuk memproses pesanan."
            )

            if st.button(
                "💳 Bayar Sekarang",
                use_container_width=True,
                key="pay_button"
            ):

                pay_order(
                    token
                )

                clear_cart()

                st.balloons()

                st.success(
                    "🎉 Pembayaran berhasil!"
                )

                st.caption(
                    "Pesanan Anda sedang diproses. Selamat menikmati kopi ☕"
                )

                st.rerun()