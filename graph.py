import json

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(style="darkgrid")

with open('recherche_locale_test.json', 'r') as fp:
    stats = json.load(fp)

# fig = figure(num=1, figsize=(15, 15))

for nom, fitness in stats.items():
    n = nom.split('_')[0]
    t = np.arange(0, len(fitness), 1)
    plt.plot(t, fitness, label=n)

plt.xlim((0, 500))
plt.show()
# max_fit = [s['max_fitness'] for s in stats]
# # label_bool = [False] * len(diff_labels)
# fig = figure(num=1, figsize=(15, 15))
# for i, y in enumerate(max_fit):
#     x = list(range(len(y)))
#
#     # color = ['b', 'r', 'g', 'y', 'c', 'm'][diff_labels.index(label[i])]
#     # if not label_bool[diff_labels.index(label[i])]:
#     #     label_bool[diff_labels.index(label[i])] = True
#     p = plt.plot(x, y, label=label[i])  # , color=color)
#     plt.plot(x, y, c=p[0].get_c())
#     # else:
#     #     plt.plot(x, y, color=color)
# plt.title(title)
# if 'ordre 1' in title or 'PMX' in title:
#     plt.xlim(0, 10000)
#     plt.ylim(-60, 0)
# else:
#     plt.xlim(0, 5000)
#     plt.ylim(0, 100)
# # plt.legend()
# ax = fig.gca()  # get the current axis
#
# # for i, p in enumerate(ax.get_lines()):  # this is the loop to change Labels and colors
# #     if p.get_label() in diff_labels[:i]:  # check for Name already exists
# #         idx = diff_labels.index(p.get_label())  # find ist index
# #         p.set_c(ax.get_lines()[idx].get_c())  # set color
# #         p.set_label('_' + p.get_label())  # hide label in auto-legend
# # plt.legend()
# plt.ylabel("fitness")
# plt.xlabel("tours")
# plt.show()
