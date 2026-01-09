import time
from sklearn.feature_extraction import DictVectorizer
from sklearn.cluster import DBSCAN
from collections import defaultdict


def group_queryset(queryset, fields=[]) -> dict:
    group_lookup = defaultdict(list)

    if fields:
        allfields = fields + ["pk"]

        values = queryset.values(*allfields)

        cluster_values = [
            {k: ("" if v is None else v) for k, v in entry.items() if k in fields}
            for entry in values
        ]

        dv = DictVectorizer()
        dv_matrix = dv.fit_transform(cluster_values)
        start = time.time()
        dbscan = DBSCAN(eps=0.1, min_samples=2, metric="manhattan")
        dbscan.fit(dv_matrix)
        print("Used " + str(time.time() - start) + "ms for dbscan")

        for idx, cluster_id in enumerate(dbscan.labels_):
            if cluster_id >= 0:
                group_lookup[int(cluster_id)].append(values[idx])

        for cluster_id in group_lookup.copy():
            first_entry = group_lookup[cluster_id][0]
            values = ", ".join(
                [f"{k}={v}" for k, v in first_entry.items() if k in fields]
            )
            new_key = f"Cluster {cluster_id}: " + values
            group_lookup[new_key] = group_lookup.pop(cluster_id)

        group_lookup = sorted(
            group_lookup.items(), key=lambda item: len(item[1]), reverse=True
        )
        return dict(group_lookup)

    return {}
