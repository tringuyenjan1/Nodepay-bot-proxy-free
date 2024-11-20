import marshal
import os

# Đường dẫn đến file đã mã hóa trong thư mục 'sr'
encrypted_file = os.path.join('sr', 'Bot.py')

# Đọc file mã hóa
with open(encrypted_file, "rb") as f:
    encrypted_code = f.read()

# Giải mã bytecode
decoded_code = marshal.loads(encrypted_code)

# Thực thi đoạn mã đã giải mã
exec(decoded_code)
