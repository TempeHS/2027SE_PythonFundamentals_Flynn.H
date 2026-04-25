import pytest
from jar import Jar

jar = Jar(5)
jar.deposit(3)
assert jar.capacity == 5
assert jar.size == 3
assert str(jar) == "🍪🍪🍪"
