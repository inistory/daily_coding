def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    for i in range(1,n):
        if phone_book[i-1] == phone_book[i][:len(phone_book[i-1])]:
            return False
    return True