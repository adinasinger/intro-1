def katie_favs(file_name):
	with open(file_name) as my_file:
		katie_favs = my_file.readlines()
	print katie_favs

def adina_favs(file_name):
	with open(file_name) as my_file:
		adina_favs = my_file.readlines()
	print adina_favs

katie_favs("katie_fav_foods.txt")
adina_favs("adina_fav_foods.txt")


def compare_fav(file_name1, file_name2):
	with open(file_name1) as katie_file:
		katie_favs = katie_file.readlines()

	with open(file_name2) as adina_file:
		adina_favs = adina_file.readlines()

	# for item in katie_favs:

	if katie_favs[0] == adina_favs[0]:
		print "Our favorite foods are the same!"
	else:
		print "Our favorite foods are different."

compare_fav("katie_fav_foods.txt", "adina_fav_foods.txt")
