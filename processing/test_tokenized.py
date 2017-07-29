from unittest import TestCase

from processing import tokenize

class TestTokenized(TestCase):
    def test_removeTags(self):
        test_sentence1 = "je te vois <PRE_3> :>"
        test_sentence2 = "nous sommes à <PLA_4><PRE_5>"
        test_sentence3 = "<PRE_4> va à la plage =<"

        t1 = tokenize.Tokenized(test_sentence1).removeTags()
        t2 = tokenize.Tokenized(test_sentence2).removeTags()
        t3 = tokenize.Tokenized(test_sentence3).removeTags()

        with self.subTest():
            self.assertEqual("je te vois :>", t1)   # compares the 1st with the 2nd's result

        with self.subTest():
            self.assertEqual("nous sommes à", t2)

        with self.subTest():
            self.assertEqual("va à la plage =<", t3)

    def test_splitWithSmileys(self):

        test_sentence1 = "j'suis tjrs à la plage:D"
        test_sentence2 = ":-)ouaih"
        test_sentence3 = "je t'<3 mon amourXP"
        test_sentence4 = "XDlol"
        test_sentence5 = "je t'espère demain^^d'acc?"
        test_sentence6 = ":):):) demain ? ;-DDDD"

        t1 = tokenize.Tokenized(test_sentence1).splitWithSmileys()
        t2 = tokenize.Tokenized(test_sentence2).splitWithSmileys()
        t3 = tokenize.Tokenized(test_sentence3).splitWithSmileys()
        t4 = tokenize.Tokenized(test_sentence4).splitWithSmileys()
        t5 = tokenize.Tokenized(test_sentence5).splitWithSmileys()
        t6 = tokenize.Tokenized(test_sentence6).splitWithSmileys()

        with self.subTest():
            self.assertEqual("j'suis tjrs à la plage :D", t1)

        with self.subTest():
            self.assertEqual(":-) ouaih", t2)

        with self.subTest():
            self.assertEqual("je t' <3 mon amour XP", t3)

        with self.subTest():
            self.assertEqual("XD lol", t4)

        with self.subTest():
            self.assertEqual("je t'espère demain ^^d 'acc?", t5)

        with self.subTest():
            self.assertEqual(":) :) :) demain ? ;-DDDD", t6)

    def test_splitWithApostrophe(self):

        test_sentence1 = "j'suis tjrs à la plage"
        test_sentence2 = "j't'suis"
        test_sentence3 = "on l'a :'D vu"
        test_sentence4 = "demain d'acc?"

        t1 = tokenize.Tokenized(test_sentence1).splitWithApostrophe()
        t2 = tokenize.Tokenized(test_sentence2).splitWithApostrophe()
        t3 = tokenize.Tokenized(test_sentence3).splitWithApostrophe()
        t4 = tokenize.Tokenized(test_sentence4).splitWithApostrophe()

        with self.subTest():
            self.assertEqual("j' suis tjrs à la plage", t1)

        with self.subTest():
            self.assertEqual("j' t' suis", t2)

        with self.subTest():
            self.assertEqual("on l' a :'D vu", t3)

        with self.subTest():
            self.assertEqual("demain d' acc?", t4)

    def test_splitWithPunctuation(self):

        test_sentence1 = "nous verrons demain."
        test_sentence2 = "tu penses?!??!? je l'avais omis..."
        test_sentence3 = "je te pense..."
        test_sentence4 = "nous nous penserons:)"

        t1 = tokenize.Tokenized(test_sentence1).splitWithPunctuation()
        t2 = tokenize.Tokenized(test_sentence2).splitWithPunctuation()
        t3 = tokenize.Tokenized(test_sentence3).splitWithPunctuation()
        t4 = tokenize.Tokenized(test_sentence4).splitWithPunctuation()

        with self.subTest():
            self.assertEqual("nous verrons demain .", t1)

        with self.subTest():
            self.assertEqual("tu penses ?!??!? je l'avais omis ...", t2)

        with self.subTest():
            self.assertEqual("je te pense ...", t3)

        with self.subTest():
            self.assertEqual("nous nous penserons :)", t4)

    def test_formatter(self):

        test_sentence1 = "je te pense...;')"
        test_sentence2 = "...et toi?"

        t1 = tokenize.Tokenized(test_sentence1).process()
        t2 = tokenize.Tokenized(test_sentence2).process()

        with self.subTest():
            self.assertEqual("je te pense ... ;')", t1)

        with self.subTest():
            self.assertEqual("... et toi ?", t2)