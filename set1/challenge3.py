__author__ = 'christianvriens'
__license__ = ''

import utils
from codecs import encode, decode

# Challenge 3 Single byte xor cipher
## Test from challenge 2
input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


x = '1c'
y = '68'

result = utils.xor_two_hex(x,y)
bin_x = bin(int(x,16))
bin_y = bin(int(y,16))
bin_result = bin(int(result,16))
print('test voor challenge 3')
print(bin_x)
print(bin_y)
print(bin_result)

## Code to revers the test above
print(x,y,result)

int_y = int(y,16)
int_x = int(x,16)
int_result = int(result,16)
unxor_result = hex((int_x^int_result)).lstrip("0x").rstrip("L")

print(decode(unxor_result,'hex'))
print(bin(int(unxor_result,16)))
print(unxor_result)

## unxor van het cipher op basis van engelse taal

from collections import Counter
cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
c = [cipher[i:i+2] for i in range(0, len(cipher), 2)]
l = Counter(c)
print('hieronder de cipher in stukjes')
print(l)
print('sorted counter')
p = l.most_common(10)
random_text = "Am terminated it excellence invitation projection as. She graceful shy believed distance use nay. Lively is people so basket ladies window expect. Supply as so period it enough income he genius. Themselves acceptance bed sympathize get dissimilar way admiration son. Design for are edward regret met lovers. This are calm case roof and. Put all speaking her delicate recurred possible. Set indulgence inquietude discretion insensible bed why announcing. Middleton fat two satisfied additions. So continued he or commanded household smallness delivered. Door poor on do walk in half. Roof his head the what. Terminated principles sentiments of no pianoforte if projection impossible. Horses pulled nature favour number yet highly his has old. Contrasted literature excellence he admiration impression insipidity so. Scale ought who terms after own quick since. Servants margaret husbands to screened in throwing. Imprudence oh an collecting partiality. Admiration gay difficulty unaffected how. Little afraid its eat looked now. Very ye lady girl them good me make. It hardly cousin me always. An shortly village is raising we shewing replied. She the favourable partiality inhabiting travelling impression put two. His six are entreaties instrument acceptance unsatiable her. Amongst as or on herself chapter entered carried no. Sold old ten are quit lose deal his sent. You correct how sex several far distant believe journey parties. We shyness enquire uncivil affixed it carried to. Is we miles ready he might going. Own books built put civil fully blind fanny. Projection appearance at of admiration no. As he totally cousins warrant besides ashamed do. Therefore by applauded acuteness supported affection it. Except had sex limits county enough the figure former add. Do sang my he next mr soon. It merely waited do unable. Spoke as as other again ye. Hard on to roof he drew. So sell side ye in mr evil. Longer waited mr of nature seemed. Improving knowledge incommode objection me ye is prevailed principle in. Impossible alteration devonshire to is interested stimulated dissimilar. To matter esteem polite do if. Started his hearted any civilly. So me by marianne admitted speaking. Men bred fine call ask. Cease one miles truth day above seven. Suspicion sportsmen provision suffering mrs saw engrossed something. Snug soon he on plan in be dine some. Difficulty on insensible reasonable in. From as went he they. Preference themselves me as thoroughly partiality considered on in estimating. Middletons acceptance discovered projecting so is so or. In or attachment inquietude remarkably comparison at an. Is surrounded prosperous stimulated am me discretion expression. But truth being state can she china widow. Occasional preference fat remarkably now projecting uncommonly dissimilar. Sentiments projection particular companions interested do at my delightful. Listening newspaper in advantage frankness to concluded unwilling. Paid was hill sir high. For him precaution any advantages dissimilar comparison few terminated projecting. Prevailed discovery immediate objection of ye at. Repair summer one winter living feebly pretty his. In so sense am known these since. Shortly respect ask cousins brought add tedious nay. Expect relied do we genius is. On as around spirit of hearts genius. Is raptures daughter branched laughter peculiar in settling. Doubtful two bed way pleasure confined followed. Shew up ye away no eyes life or were this. Perfectly did suspicion daughters but his intention. Started on society an brought it explain. Position two saw greatest stronger old. Pianoforte if at simplicity do estimating. "
k = utils.character_counter(random_text)
r = k.most_common(11)
print(r)

print('lijst met XOR van cipher top 10 vs taal top 10 uit cipher')
x = '37'
y = encode(b'e','hex')
result = utils.xor_two_hex(x,y)
uncipher = '82'

unxor = utils.xor_two_hex(cipher,uncipher)
print(unxor)
chr_unxor = chr(int(unxor,16))
str_unxor = str(unxor)
print(str_unxor.decode("hex"))



