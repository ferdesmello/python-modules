# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ferde-so <ferde-so@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/13 01:56:49 by ferde-so          #+#    #+#              #
#    Updated: 2026/08/13 01:58:56 by ferde-so         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	total_harvest = 0
	total_harvest += int(input("Day 1 harvest: "))
	total_harvest += int(input("Day 2 harvest: "))
	total_harvest += int(input("Day 3 harvest: "))
	print("Total harvest:", total_harvest)