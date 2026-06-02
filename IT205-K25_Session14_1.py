# Giá trị 15000 đang gán cho tham số discount, giá trị 0.1 đang gán cho tham số shipping_fee.
# Lỗi này khiến giá trị giảm giá bị nhân lên 15000 lần (1.500.000%), dẫn đến kết quả bị âm.
# Dòng lệnh lỗi do thực hiện phép cộng giữa một giá trị rỗng (NoneType) và một số nguyên (int).
# Biến order_total mang giá trị None vì hàm calculate_final_price không sử dụng lệnh return để trả kết quả.
# Hàm print chỉ hiển thị chữ ra màn hình, còn return giúp giữ lại giá trị để tính toán tiếp.
# Cần thay print bằng return ở cuối hàm và gọi hàm theo đúng thứ tự các tham số đầu vào.


def calculate_final_price(price, discount, shipping_fee):
    return price - (price * discount) + shipping_fee

order_total = calculate_final_price(100000, 0.1, 15000)

print("Khách hàng cần thanh toán:", order_total + 5000)
