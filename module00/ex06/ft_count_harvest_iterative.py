# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ferde-so <ferde-so@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/13 02:03:50 by ferde-so          #+#    #+#              #
#    Updated: 2026/08/13 02:54:12 by ferde-so         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for day in range(1, days + 1):
        print(f"Day {day}")
    print("Harvest time!")
