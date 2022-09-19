objects = {
  "string": "",
  "list": [],
  "TypeNone": None,
  "int": 0
}
vars = {}

currentCodeLine = ""
while currentCodeLine != "sendOut":
  currentCodeLine = input()
  wordsInLine = currentCodeLine.split(" ")
  for x in range(0, (len(wordsInLine) - 1), 1): 
      if x != 0:
        if wordsInLine[x] == "is": 
          if wordsInLine[x + 1] == "object":
            vars.update({wordsInLine[x - 1]: objects[wordsInLine[x+2]]})
          elif wordsInLine[x + 1] == "function":
              if wordsInLine[x + 3] == "arguments":
                whitespacedArgs = currentCodeLine[currentCodeLine.find("arguments"):].lstrip("arguments").split(" and")
                args = []
                for arg in whitespacedArgs:
                  args.append({" ".join(arg.split()): None})
                vars.update({wordsInLine[x - 1]: args})
          elif wordsInLine[x - 1] == "output":
            if wordsInLine[x + 1] == "input":
              print(input())
            elif vars.get(wordsInLine[x + 1]) is not None:
              if (x + 2) < len(wordsInLine) and vars.get(wordsInLine[x + 2]) is not None:
                print(vars.get(wordsInLine[x + 1]) + vars.get(wordsInLine[x + 2]))
              else:
                print(vars.get(wordsInLine[x + 1]))
            else:
              print(" ".join(wordsInLine[x+1:]))
          elif wordsInLine[x + 1] == "input":
            if vars.get(wordsInLine[x - 1]) is not None:
              vars[wordsInLine[x - 1]] = input()
            else:
              vars.update({wordsInLine[x - 1]: input()})
          elif vars.get(wordsInLine[x + 1]) is not None: #ex. hat is the boy, small is hat == small is the boy
            vars.update({wordsInLine[x - 1]: vars.get(wordsInLine[x+1])})
          elif vars.get(wordsInLine[x - 1]) is not None: #ex. hat is child, hat is human == hat is human
            vars[wordsInLine[x-1]] = wordsInLine[x + 1]
          elif wordsInLine[x - 1].isnumeric(): # ex. 9 is 5 == False
            if int(wordsInLine[x - 1]) == int(wordsInLine[x + 1]):
              vars.update({("%s=%s" % (wordsInLine[x-1], wordsInLine[x + 1])): True})
            else:
              vars.update({("%s=%s" % (wordsInLine[x-1], wordsInLine[x + 1])): False})
          else:
            vars.update({wordsInLine[x - 1]: " ".join(wordsInLine[x+1:])}) 
print(vars)
# search is function with arguments key and list
# search definition:
#	results is object list
#	scenario entry is object string following each of list:
#		scenario entry has key:
#			results is with entry
#	product is results

# entries is object list
# output is “What would you like to search for?”
# results is search with key of input and list of entries:
# scenario result is string following each of results:
#	output is result