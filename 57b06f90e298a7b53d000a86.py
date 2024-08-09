def queue_time(customers, n):
    if not customers:
        return 0

    tills = [0] * n

    for customer in customers:
        tills[tills.index(min(tills))] += customer

    return max(tills)
