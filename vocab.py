# vocab.py
import random
import numpy as np
import GetText
'''
    A default vocab implementation and base class, to provide random letters and numbers.
'''
class Vocab():
    def __init__(self):
        tex = GetText.get62ExampleText()
        #self.vocab = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"+tex
        self.vocab=tex
        self.size = len(self.vocab)
        print('size',self.size)
        indices = range(self.size)
        self.index = dict(zip(self.vocab, indices))
    # return random string by given length
    def rand_string(self, length):
        # if len(vocab) == 0 raise exception
        return "".join(random.sample(self.vocab, length))
    # get symbol (char in vocabulary) by its ordinal
    def get_sym(self, idx):
        # if idx >= len(self.vocab) raise exception
        return self.vocab[idx]
    # given a symbol, return its ordinal in given vocabulary.
    def get_index(self, sym):
        return self.index[sym]
    # given 'abc', return [10, 11, 12]
    def to_indices(self, text):
        return [self.index[c] for c in text]
    # given [10, 11, 12], return 'abc'
    def to_text(self, indices):
        return "".join([self.vocab[i] for i in indices])
    # given '01', return vector [1 0 0 0 0 0 0 0 0 0 ... 0 \n 0 1 0 0 0 0 ... 0]
    #定义一个由元素个数确定行数，self.vocab确定列的一个二维数组（矩阵）
    def text_to_one_hot(self, text):
        #print('--->',self.to_indices(text))
        num_labels = np.array(self.to_indices(text))
        n = len(text)                           #长度
        #print("n=",n)
        categorical = np.zeros((n, self.size)) #创建全是0 的矩阵
        #print('--=?>',categorical)
        categorical[np.arange(n), num_labels] = 1   #给元素所在的位置赋值1
        #print('==?>',categorical)
        return categorical.ravel()
    # translate one hot vector to text.
    def one_hot_to_text(self, onehots):
        text_len = onehots.shape[0] // self.size
        onehots = np.reshape(onehots, (text_len, self.size))
        indices = np.argmax(onehots, axis = 1)
        return self.to_text(indices)
if __name__ == "__main__":
    # test code
    vocab = Vocab()
    print(vocab.rand_string(4))
    print(vocab.get_sym(10))
    print(vocab.get_index('网'))
    print(vocab.size)
    print(vocab.text_to_one_hot("相账黄"))
