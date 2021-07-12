def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    for i in range(n):
        if phone_book[i-1] in phone_book[i][:len(phone_book[i-1])]:
            return False
    return True