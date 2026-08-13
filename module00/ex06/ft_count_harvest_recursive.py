# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ferde-so <ferde-so@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/13 02:04:01 by ferde-so          #+#    #+#              #
#    Updated: 2026/08/13 02:37:25 by ferde-so         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(days=None, day=1):
	if days is None:
		days = int(input("Days until harvest: "))
	if day <= days:
		print(f"Day {day}")
		ft_count_harvest_recursive(days, day + 1)
	else:
		print("Harvest time!")