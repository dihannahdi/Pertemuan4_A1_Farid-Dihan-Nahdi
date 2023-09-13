banyak_data = int(input())				# 5
jumlah = 0

for i in range(1, banyak_data + 1):
	data = int(input())					# 3 4 7 2 9
	jumlah = jumlah + data
	
print(jumlah // banyak_data)