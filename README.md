# Uncommon Error in Python: ZeroDivisionError
This repository demonstrates an example of a `ZeroDivisionError` in Python, which can sometimes be subtle and hard to catch. The focus is on handling a particular type of error that may not always be immediately apparent.

## The Problem
The `function_with_uncommon_error` function attempts to handle the case where `a` or `b` is zero.  However, it will still raise a `ZeroDivisionError` if `b` is zero unless it is handled explicitly. This type of error is not always immediately obvious if you don't focus on the exact scenario when 'b' is zero.

## The Solution
The solution improves error handling by explicitly checking if `b` is zero before performing the division, thus preventing the error.