import answers

def includes(question, keywords):
	for word in keywords:
		if (word not in question):
			return False
	return True

def evaluate(question):
	for i in range (0, len(answers["keygroups"])):
		if (includes(question, keygroups[i]["keywords"])):
			answer = keygroups[i]["answer"]
			while (answer == ""):
				i -= 1
				answer = keygroups[i]["answer"]
			return answer
	return answers.default_answer