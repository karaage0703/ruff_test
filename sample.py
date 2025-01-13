from typing import Dict, List


def calculate_sum(numbers: List[int]) -> int:
    total = 0
    for num in numbers:
        total += num  # 不適切なスペース
    return total


def process_data(
    data: Dict[str, any],
) -> None:  # anyは小文字で使用されており、型アノテーションとして正しくない
    if data["status"] == "success":  # 不適切なスペース、シングルクォートの使用
        print("Processing successful data...")
        values = [1, 2, 3, 4, 5]  # 不適切なスペース
        result = calculate_sum(values)
        print(f"Result: {result}")
    else:
        print("Error in processing")  # 不適切なスペース、シングルクォートの使用


if __name__ == "__main__":  # シングルクォートの使用
    test_data = {"status": "success"}  # 不適切なスペース
    example_variable = (
        "This is an example of a line that slightly exceeds the 127-character xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx."
    )
    process_data(test_data)
