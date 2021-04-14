def solution(phone_book):
    if not phone_book:
        return True

    phone_book.sort()

    # for p1, p2 in zip(phoneBook, phoneBook[1:]):
    for i in range(len(phone_book) - 1):
        # if p2.startswith(p1):
        if phone_book[i + 1].find(phone_book[i]) == 0:
            return False

    return True


a = ["97 67 4223", "1 19", " 11 95 5244 21"]
# a = []
# a = ["97 67 4223"]
print("Answer:", solution(a))


print(a[2], a[1])
print(a[2].startswith(a[1]))
