# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ferde-so <ferde-so@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/13 02:10:10 by ferde-so          #+#    #+#              #
#    Updated: 2026/08/13 02:22:16 by ferde-so         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit == "packets":
		print(f"{seed_type} seeds: {quantity} {unit} available")
	elif unit == "grams":
		print(f"{seed_type} seeds: {quantity} {unit} total")
	elif unit == "area":
		print(f"{seed_type} seeds: covers {quantity} square meters")
	else:
		print("Unknown unit type")