# The goal of this exercise is to convert a string to a new string 
# where each character in the new string is "(" if that character appears only once in the original string,
#  or ")" if that character appears more than once in the original string. 
# Ignore capitalization when determining if a character is a duplicate.

#Examples
#"din"      =>  "((("
#"recede"   =>  "()()()"
#"Success"  =>  ")())())"
#"(( @"     =>  "))((" 
#Notes

#Assertion messages may be unclear about what they display in some languages.
# 
#  If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

def duplicate_encode(word):
    new_word =""
    for char in word.lower():
        char_count=word.lower().count(char)
        if char_count > 1:
            char = ')'
        else:
            char = '('
        new_word += char
    return new_word
# #Test Results:
# Basic tests:
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Tests with '(' and ')'
# Test Passed
# Test Passed
# And now... some random tests !
# Testing for word "TFezkRSR@T@TGvzJS!n@RzzT zP@@avz SGxam"
# Testing for word "wGuOwbSO k!x)SSzd(SzHGyxH"
# Testing for word "wcFkQzJn)bIc)c"
# Testing for word "aQ(FQ@e@O QO"
# Testing for word " HeJyvIdd"
# Testing for word "d(bzcdQc Sny(xzkxOeFG uRFxbmnH(OSH"
# Testing for word " vJdHdGQzRRnndx!TGcR"
# Testing for word ")aRHz!Im!lGl "
# Testing for word "bQmkGGOQeG bvkFHdd znQw)Im(TTQ)HubbwG"
# Testing for word "wHexySw@PPayGFO!OQ)b!G(GP"
# Testing for word "!T@uF)!TQ)S"
# Testing for word "cweIFxbu  lOOO(zO)Sa))y"
# Testing for word "!zudxQSF PclG))wm"
# Testing for word "nJevxl@)Gxb)PRvb"
# Testing for word "ldaSvIPy!PRczFR GPQbGkOOHee(HJSdd"
# Testing for word "bTcx!vQ@QIGuyluTmkdv"
# Testing for word "OukPvdml@Pdm)u OzPFexyyzk(zwv)klQ((JQ!TH"
# Testing for word "On)JndkIxJmSlbyS)GIdxFk@F"
# Testing for word "byIQkx@xeJzJO!PkbFH"
# Testing for word "TSQJewFa)yQmu!av(yT(x!"
# Testing for word "(Fuenmm@a!xJkO)vvJw"
# Testing for word "OSa!nuJ(@dSRuG !)c )dOTQ"
# Testing for word "HScFyOQF!FFT!PdGFPObFz zy)mRlb)bc"
# Testing for word " JF  v)RwF"
# Testing for word "wkF!dzJJHd"
# Testing for word "mzTH(JzwkPl)R)GkeH"
# Testing for word "akFSGFQ()lTJGTdwlzQRJJvvxuvv"
# Testing for word "kmaa vIvnay"
# Testing for word ")mIIvw@vwP!SaGSPOxy(Rz "
# Testing for word "wkw)F)z)QaJzyIbePFmT"
# Testing for word "Ou b!QOm@ISI"
# Testing for word "GkQGGFaczmPIT@v!OawwSGldkaayxJPczTJe!FO)"
# Testing for word "Q(HcdHdwxy@PR@u(eQu!!SewH "
# Testing for word "!PalJIxI@yzSIPO(JHJRnRzlm!lSS!mIHFJuT"
# Testing for word "FwIkSFeyxbIlvbdFPGccab!zxIGc@uwRwybPT"
# Testing for word "Txm!TbIOcnGHRwHInOQH(n@a(mOaJebdmRcndx"
# Testing for word "y SnmkIQHyFeJecSly@@bTGvTSm@mlIPyxd@Sa"
# Testing for word "HyOFGJTkmHzdc"
# Testing for word "y!J)IedlHTJTwS"
# Testing for word "@azQTQJzc(mFzOzayz!cFJveS"
# You have passed all of the tests! :)