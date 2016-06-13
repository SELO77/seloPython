import ujson as uj

st = """
{
  "list": [
    {
      "name": "selo"
    },
    {
      "name": "serim"
    },
    {
      "name": "garo"
    }
  ]
}
"""

result = uj.loads(st)
print(result)