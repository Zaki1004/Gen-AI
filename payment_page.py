# import streamlit as st

# from services.payment_service import (
#     pay_order,
#     get_order
# )

# st.set_page_config(
#     page_title="Coffee Payment",
#     page_icon="☕"
# )

# token = st.query_params.get(
#     "payment"
# )

# st.title(
#     "☕ Coffee Payment"
# )

# if not token:

#     st.info(
#         "Silahkan scan QR Code untuk melakukan pembayaran"
#     )

#     st.stop()

# order = get_order(token)

# if not order:

#     st.error(
#         "Order tidak ditemukan"
#     )

#     st.stop()

# order_id = order[0]
# status = order[1]
# total_price = order[2]

# st.subheader(
#     f"Order #{order_id}"
# )

# st.metric(
#     "Total Pembayaran",
#     f"Rp{total_price:,}"
# )

# if status == "paid":

#     st.success(
#         "✅ Status: PAID"
#     )

# else:

#     st.warning(
#         "⏳ Status: UNPAID"
#     )

#     if st.button(
#         "💳 Bayar Sekarang"
#     ):

#         success = pay_order(
#             token
#         )

#         if success:

#             st.success(
#                 "Pembayaran berhasil"
#             )

#         else:

#             st.error(
#                 "Gagal melakukan pembayaran"
#             )

#         st.rerun()