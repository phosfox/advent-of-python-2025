
def part1(input)
  lines = File.read_lines(input)
  problems = [] of Array(String)
  lines.each do |line|
    problems << line.split()
  end
  total = 0_i64
  problems.transpose().each do |problem|
    result = solve_problem(problem)
    total += result
  end
  puts total
end

def part22(input)
  lines = File.read_lines(input)
  problems = [] of Array(Char)
  lines.each do |line|
    p! line
    chars = [] of Char
    line.each_char do |ch|
      chars << ch
    end
    problems << chars
  end
  p! problems.transpose()
end

def part2(input)
  lines = File.read_lines(input)
  problems = [] of Array(String)
  lines.each do |line|
    problems << line.split()
  end

  total = 0_i64
  problems.transpose().each do |problem|
    ps = [] of Array(String)
    operator = problem[-1]
    problem[..-2].each do |s|
      ps << padd(s).chars.map { |ch| ch.to_s }
    end
    puts ps

    nums = [] of Int64
    (0...4).each do |idx|
      s = (takeLastNth(idx, ps)).strip()
      if s.size != 0
         nums << s.to_i64
      end
    end
    puts nums
    result = solve_problem(nums)
    puts result
    total += result
  end
  puts total

end

def padd(s : String, max_size = 4)
  len = s.size
  return s + " " * (max_size - len)
end

def takeLastNth(n, arrs : Array(Array(String)))
  res = ""
  arrs.each do |arr|
    res += arr[n]
  end
  return res
end

def solve_problem(problem)
  operator = problem[-1]
  nums = [] of Int64
  problem[..-2].each do |num|
    nums << (num.to_i)
  end
  if operator == "+"
    return nums.sum()
  else
    return nums.product()
  end
end

part1("inputs/day06.txt")
part22("inputs/day06_test.txt")
