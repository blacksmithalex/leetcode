class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        sentence = sentence.split()
        for i in range(len(sentence)):
            word = sentence[i]
            if word[0].lower() in 'aeiou':
                sentence[i] = word + 'ma' + 'a' * (i + 1)
            else:
                sentence[i] = word[1:] + word[0] + 'ma' + 'a' * (i + 1)
        return ' '.join(sentence)

