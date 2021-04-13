adj = {
    0: [1, 2, 5],
    1: [3, 2, 0],
    2: [1, 4, 0],
    3: [6, 4, 1],
    4: [3, 6, 5, 2],
    5: [4, 6, 0],
    6: [5, 4, 3]
}

AB_all = 0
AB_3 = 0
ans = []


def dfs(now, vis, path):
    global AB_all, AB_3
    path.append(now)
    if now == 6:
        AB_all += 1
        print(path)
        ans.append(path)
        if len(vis) <= 3:
            AB_3 += 1
        return
    for nxt in adj[now]:
        mn = min(nxt, now)
        mx = max(nxt, now)
        if (mn, mx) in vis:
            continue
        else:
            vis_now = vis.copy()
            vis_now.add((mn, mx))
            dfs(nxt, vis_now, path.copy())


dfs(0, set(), [])
print(AB_all)
print(AB_3)
ans.sort()
for an in ans:
    print(an)
