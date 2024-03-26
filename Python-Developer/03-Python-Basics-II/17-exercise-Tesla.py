def checkDriverAge():
	age = input("What is your age?: ")
	if int(age) < 18:
		print("Sorry, you are too young to drive this car. Powering off")
	elif int(age) > 18:
		print("Powering On. Enjoy the ride!")
	elif int(age) == 18:
		print("Congratulations on your first year of driving. Enjoy the ride!")
	else:
		print("Your age: 0")

checkDriverAge(41)


#1. Yukarıdaki kodu checkDriverAge() adlı bir fonksiyona sarın. Bu fonksiyonu her çağırdığınızda, yaşınız sorulacaktır. 
# Fonksiyonu her seferinde kopyalayıp yapıştırmak yerine checkDriverAge() kullanmanın faydasını fark ettiniz mi?

#2 input() kullanmak yerine. Şimdi, checkDriverAge() fonksiyonunun bir yaş argümanı kabul etmesini sağlayın, böylece girerseniz:
#checkDriverAge(92);
#Ayrıca, herhangi bir argüman verilmediğinde varsayılan yaşın 0 olarak ayarlanmasını sağlayın.
