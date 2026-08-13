# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ferde-so <ferde-so@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/13 01:59:25 by ferde-so          #+#    #+#              #
#    Updated: 2026/08/13 02:20:30 by ferde-so         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
	plant_age = int(input("Enter plant age in days: "))
	if plant_age <= 60:
		print("Plant needs more time to grow.")
	else:
		print("Plant is ready to harvest!")