# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ferde-so <ferde-so@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/13 01:54:02 by ferde-so          #+#    #+#              #
#    Updated: 2026/08/13 02:54:23 by ferde-so         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
    length = input("Enter length: ")
    width = input("Enter width: ")
    area = int(length) * int(width)
    print("Plot area:", area)
