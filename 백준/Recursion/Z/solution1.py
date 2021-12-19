N, r, c = map(int, input().split())

def recursive(size, left_r, left_c, r,c, count ):
    if size <=1:
        return count
    else:
        half = size//2
        if r < half and c < half:
            return recursive(half, left_r, left_c, r, c, count)
        elif r< half and c >= half:
            return recursive(half, left_r, left_c+half, r, c-half, count+half**2)
        elif r >= half and c < half:
            return recursive(half, left_r+half, left_c, r-half, c, count+2*half**2)
        else:
            return recursive(half, left_r+half, left_c+half, r-half, c-half, count+3*half**2)


result = recursive(2**N, 0,0,r,c, 0)
print(result, end=" ")