def find_duplicate(nums):
    nums = sorted(nums)

    for index in range(1, len(nums)):
        if not isinstance(nums[index], int) or nums[index] < 0:
            return False

        if nums[index] == nums[index - 1]:
            return nums[index]

    return False
