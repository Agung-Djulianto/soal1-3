def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Contoh penggunaan
nums1 = [2, 2, 1]
print("Output:", singleNumber(nums1))  # Output: 1

nums2 = [4, 1, 2, 1, 2]
print("Output:", singleNumber(nums2))  # Output: 4
