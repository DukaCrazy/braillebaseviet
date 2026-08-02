from braillebase import *

class BrailleBaseViet(BrailleBase):
    def __init__(self):

        """
        """
        super().__init__()
        self.setting_braille_rules_uppercase("⠠", "⠠⠠") #2026/05/18
        #letras min
        self.append_braille_letter("a", ["⠁"]) #2026/06/09
        self.append_braille_letter("b", ["⠃"]) #2026/06/09
        self.append_braille_letter("c", ["⠉"]) #2026/06/09
        self.append_braille_letter("d", ["⠙"]) #2026/06/09
        self.append_braille_letter("e", ["⠑"]) #2026/06/09
        self.append_braille_letter("f", ["⠋"]) #2026/06/09
        self.append_braille_letter("g", ["⠛"]) #2026/06/09
        self.append_braille_letter("h", ["⠓"]) #2026/06/09
        self.append_braille_letter("i", ["⠊"]) #2026/06/09
        self.append_braille_letter("j", ["⠚"]) #2026/06/09
        self.append_braille_letter("k", ["⠅"]) #2026/06/09
        self.append_braille_letter("l", ["⠇"]) #2026/06/09
        self.append_braille_letter("m", ["⠍"]) #2026/06/09
        self.append_braille_letter("n", ["⠝"]) #2026/06/09
        self.append_braille_letter("o", ["⠕"]) #2026/06/09
        self.append_braille_letter("p", ["⠏"]) #2026/06/09
        self.append_braille_letter("q", ["⠟"]) #2026/06/09
        self.append_braille_letter("r", ["⠗"]) #2026/06/09
        self.append_braille_letter("s", ["⠎"]) #2026/06/09
        self.append_braille_letter("t", ["⠞"]) #2026/06/09
        self.append_braille_letter("u", ["⠥"]) #2026/06/09
        self.append_braille_letter("v", ["⠧"]) #2026/06/09
        self.append_braille_letter("w", ["⠺"]) #2026/06/09
        self.append_braille_letter("x", ["⠭"]) #2026/06/09
        self.append_braille_letter("y", ["⠽"]) #2026/06/09
        self.append_braille_letter("z", ["⠵"]) #2026/06/09
        #Viet
        self.append_braille_letter("ă", ["⠜"]) #2026/08/01
        self.append_braille_letter("â", ["⠡"]) #2026/08/01
        self.append_braille_letter("ê", ["⠣"]) #2026/08/01
        self.append_braille_letter("ô", ["⠹"]) #2026/08/01
        self.append_braille_letter("ơ", ["⠪"]) #2026/08/01
        self.append_braille_letter("ư", ["⠳"]) #2026/08/01

        self.append_braille_letter("á", ["⠁"]) #2026/08/01
        self.append_braille_letter("ắ", ["⠜"]) #2026/08/01
        self.append_braille_letter("ấ", ["⠡"]) #2026/08/01
        self.append_braille_letter("à", ["⠁"]) #2026/08/01
        self.append_braille_letter("ằ", ["⠜"]) #2026/08/01
        self.append_braille_letter("ầ", ["⠡"]) #2026/08/01
        self.append_braille_letter("ả", ["⠁"]) #2026/08/01
        self.append_braille_letter("ẳ", ["⠜"]) #2026/08/01
        self.append_braille_letter("ẩ", ["⠡"]) #2026/08/01
        self.append_braille_letter("ã", ["⠁"]) #2026/08/01
        self.append_braille_letter("ẵ", ["⠜"]) #2026/08/01
        self.append_braille_letter("ẫ", ["⠡"]) #2026/08/01
        self.append_braille_letter("ạ", ["⠁"]) #2026/08/01
        self.append_braille_letter("ặ", ["⠜"]) #2026/08/01
        self.append_braille_letter("ậ", ["⠡"]) #2026/08/01

        self.append_braille_letter("đ", ["⠮"]) #2026/08/01

        self.append_braille_letter("é", ["⠑"]) #2026/08/01
        self.append_braille_letter("ế", ["⠣"]) #2026/08/01
        self.append_braille_letter("è", ["⠑"]) #2026/08/01
        self.append_braille_letter("ề", ["⠣"]) #2026/08/01
        self.append_braille_letter("ẻ", ["⠑"]) #2026/08/01
        self.append_braille_letter("ể", ["⠣"]) #2026/08/01
        self.append_braille_letter("ẽ", ["⠑"]) #2026/08/01
        self.append_braille_letter("ễ", ["⠣"]) #2026/08/01
        self.append_braille_letter("ẹ", ["⠑"]) #2026/08/01
        self.append_braille_letter("ệ", ["⠣"]) #2026/08/01

        self.append_braille_letter("í", ["⠊"]) #2026/08/01
        self.append_braille_letter("ì", ["⠊"]) #2026/08/01
        self.append_braille_letter("ỉ", ["⠊"]) #2026/08/01
        self.append_braille_letter("ĩ", ["⠊"]) #2026/08/01
        self.append_braille_letter("ị", ["⠊"]) #2026/08/01

        self.append_braille_letter("ó", ["⠕"]) #2026/08/01
        self.append_braille_letter("ố", ["⠹"]) #2026/08/01
        self.append_braille_letter("ớ", ["⠪"]) #2026/08/01
        self.append_braille_letter("ò", ["⠕"]) #2026/08/01
        self.append_braille_letter("ồ", ["⠹"]) #2026/08/01
        self.append_braille_letter("ờ", ["⠪"]) #2026/08/01
        self.append_braille_letter("ỏ", ["⠕"]) #2026/08/01
        self.append_braille_letter("ổ", ["⠹"]) #2026/08/01
        self.append_braille_letter("ở", ["⠪"]) #2026/08/01
        self.append_braille_letter("õ", ["⠕"]) #2026/08/01
        self.append_braille_letter("ỗ", ["⠹"]) #2026/08/01
        self.append_braille_letter("ỡ", ["⠪"]) #2026/08/01
        self.append_braille_letter("ọ", ["⠕"]) #2026/08/01
        self.append_braille_letter("ộ", ["⠹"]) #2026/08/01
        self.append_braille_letter("ợ", ["⠪"]) #2026/08/01

        self.append_braille_letter("ú", ["⠥"]) #2026/08/01
        self.append_braille_letter("ứ", ["⠳"]) #2026/08/01
        self.append_braille_letter("ù", ["⠥"]) #2026/08/01
        self.append_braille_letter("ừ", ["⠳"]) #2026/08/01
        self.append_braille_letter("ủ", ["⠥"]) #2026/08/01
        self.append_braille_letter("ử", ["⠳"]) #2026/08/01
        self.append_braille_letter("ũ", ["⠥"]) #2026/08/01
        self.append_braille_letter("ữ", ["⠳"]) #2026/08/01
        self.append_braille_letter("ụ", ["⠥"]) #2026/08/01
        self.append_braille_letter("ự", ["⠳"]) #2026/08/01

        self.append_braille_letter("ý", ["⠽"]) #2026/08/01
        self.append_braille_letter("ỳ", ["⠽"]) #2026/08/01
        self.append_braille_letter("ỷ", ["⠽"]) #2026/08/01
        self.append_braille_letter("ỹ", ["⠽"]) #2026/08/01
        self.append_braille_letter("ỵ", ["⠽"]) #2026/08/01


       #letras maiusc
        self.append_braille_letter("A", ["⠁"],1) #2026/06/09
        self.append_braille_letter("B", ["⠃"],1) #2026/06/09
        self.append_braille_letter("C", ["⠉"],1) #2026/06/09
        self.append_braille_letter("D", ["⠙"],1) #2026/06/09
        self.append_braille_letter("E", ["⠑"],1) #2026/06/09
        self.append_braille_letter("F", ["⠋"],1) #2026/06/09
        self.append_braille_letter("G", ["⠛"],1) #2026/06/09
        self.append_braille_letter("H", ["⠓"],1) #2026/06/09
        self.append_braille_letter("I", ["⠊"],1) #2026/06/09
        self.append_braille_letter("J", ["⠚"],1) #2026/06/09
        self.append_braille_letter("K", ["⠅"],1) #2026/06/09
        self.append_braille_letter("L", ["⠇"],1) #2026/06/09
        self.append_braille_letter("M", ["⠍"],1) #2026/06/09
        self.append_braille_letter("N", ["⠝"],1) #2026/06/09
        self.append_braille_letter("O", ["⠕"],1) #2026/06/09
        self.append_braille_letter("P", ["⠏"],1) #2026/06/09
        self.append_braille_letter("Q", ["⠟"],1) #2026/06/09
        self.append_braille_letter("R", ["⠗"],1) #2026/06/09
        self.append_braille_letter("S", ["⠎"],1) #2026/06/09
        self.append_braille_letter("T", ["⠞"],1) #2026/06/09
        self.append_braille_letter("U", ["⠥"],1) #2026/06/09
        self.append_braille_letter("V", ["⠧"],1) #2026/06/09
        self.append_braille_letter("W", ["⠺"],1) #2026/06/09
        self.append_braille_letter("X", ["⠭"],1) #2026/06/09
        self.append_braille_letter("Y", ["⠽"],1) #2026/06/09
        self.append_braille_letter("Z", ["⠵"],1) #2026/06/09
        #Viet
        self.append_braille_letter("ă", ["⠜"], 1) #2026/08/01
        self.append_braille_letter("Â", ["⠡"], 1) #2026/08/01
        self.append_braille_letter("Ê", ["⠣"], 1) #2026/08/01
        self.append_braille_letter("Ô", ["⠹"], 1) #2026/08/01
        self.append_braille_letter("Ơ", ["⠪"], 1) #2026/08/01
        self.append_braille_letter("Ư", ["⠳"], 1) #2026/08/01

        self.append_braille_letter("Á", ["⠁"], 1) #2026/08/01
        self.append_braille_letter("Ắ", ["⠜"], 1) #2026/08/01
        self.append_braille_letter("Ấ", ["⠡"], 1) #2026/08/01
        self.append_braille_letter("À", ["⠁"], 1) #2026/08/01
        self.append_braille_letter("Ằ", ["⠜"], 1) #2026/08/01
        self.append_braille_letter("Ầ", ["⠡"], 1) #2026/08/01
        self.append_braille_letter("Ả", ["⠁"], 1) #2026/08/01
        self.append_braille_letter("Ẳ", ["⠜"], 1) #2026/08/01
        self.append_braille_letter("Ẩ", ["⠡"], 1) #2026/08/01
        self.append_braille_letter("Ã", ["⠁"], 1) #2026/08/01
        self.append_braille_letter("Ẵ", ["⠜"], 1) #2026/08/01
        self.append_braille_letter("Ẫ", ["⠡"], 1) #2026/08/01
        self.append_braille_letter("Ạ", ["⠁"], 1) #2026/08/01
        self.append_braille_letter("Ặ", ["⠜"], 1) #2026/08/01
        self.append_braille_letter("Ậ", ["⠡"], 1) #2026/08/01

        self.append_braille_letter("Đ", ["⠮"], 1) #2026/08/01

        self.append_braille_letter("É", ["⠑"], 1) #2026/08/01
        self.append_braille_letter("Ế", ["⠣"], 1) #2026/08/01
        self.append_braille_letter("È", ["⠑"], 1) #2026/08/01
        self.append_braille_letter("Ề", ["⠣"], 1) #2026/08/01
        self.append_braille_letter("Ẻ", ["⠑"], 1) #2026/08/01
        self.append_braille_letter("Ể", ["⠣"], 1) #2026/08/01
        self.append_braille_letter("Ẽ", ["⠑"], 1) #2026/08/01
        self.append_braille_letter("Ễ", ["⠣"], 1) #2026/08/01
        self.append_braille_letter("Ẹ", ["⠑"], 1) #2026/08/01
        self.append_braille_letter("Ệ", ["⠣"], 1) #2026/08/01

        self.append_braille_letter("Í", ["⠊"], 1) #2026/08/01
        self.append_braille_letter("Ì", ["⠊"], 1) #2026/08/01
        self.append_braille_letter("Ỉ", ["⠊"], 1) #2026/08/01
        self.append_braille_letter("Ĩ", ["⠊"], 1) #2026/08/01
        self.append_braille_letter("Ị", ["⠊"], 1) #2026/08/01

        self.append_braille_letter("Ó", ["⠕"], 1) #2026/08/01
        self.append_braille_letter("Ố", ["⠹"], 1) #2026/08/01
        self.append_braille_letter("Ớ", ["⠪"], 1) #2026/08/01
        self.append_braille_letter("Ò", ["⠕"], 1) #2026/08/01
        self.append_braille_letter("Ồ", ["⠹"], 1) #2026/08/01
        self.append_braille_letter("Ờ", ["⠪"], 1) #2026/08/01
        self.append_braille_letter("Ỏ", ["⠕"], 1) #2026/08/01
        self.append_braille_letter("Ổ", ["⠹"], 1) #2026/08/01
        self.append_braille_letter("Ở", ["⠪"], 1) #2026/08/01
        self.append_braille_letter("Õ", ["⠕"], 1) #2026/08/01
        self.append_braille_letter("Ỗ", ["⠹"], 1) #2026/08/01
        self.append_braille_letter("Ỡ", ["⠪"], 1) #2026/08/01
        self.append_braille_letter("Ọ", ["⠕"], 1) #2026/08/01
        self.append_braille_letter("Ộ", ["⠹"], 1) #2026/08/01
        self.append_braille_letter("Ợ", ["⠪"], 1) #2026/08/01

        self.append_braille_letter("Ú", ["⠥"], 1) #2026/08/01
        self.append_braille_letter("Ứ", ["⠳"], 1) #2026/08/01
        self.append_braille_letter("Ù", ["⠥"], 1) #2026/08/01
        self.append_braille_letter("Ừ", ["⠳"], 1) #2026/08/01
        self.append_braille_letter("Ủ", ["⠥"], 1) #2026/08/01
        self.append_braille_letter("Ử", ["⠳"], 1) #2026/08/01
        self.append_braille_letter("Ũ", ["⠥"], 1) #2026/08/01
        self.append_braille_letter("Ữ", ["⠳"], 1) #2026/08/01
        self.append_braille_letter("Ụ", ["⠥"], 1) #2026/08/01
        self.append_braille_letter("Ự", ["⠳"], 1) #2026/08/01

        self.append_braille_letter("Ý", ["⠽"], 1) #2026/08/01
        self.append_braille_letter("Ỳ", ["⠽"], 1) #2026/08/01
        self.append_braille_letter("Ỷ", ["⠽"], 1) #2026/08/01
        self.append_braille_letter("Ỹ", ["⠽"], 1) #2026/08/01
        self.append_braille_letter("Ỵ", ["⠽"], 1) #2026/08/01

        #number
        self.append_braille_letter("⠼", ["⠼"]) #2026/06/09
        self.append_braille_letter("1", ["⠁"]) #2026/06/09
        self.append_braille_letter("2", ["⠃"]) #2026/06/09
        self.append_braille_letter("3", ["⠉"]) #2026/06/09
        self.append_braille_letter("4", ["⠙"]) #2026/06/09
        self.append_braille_letter("5", ["⠑"]) #2026/06/09
        self.append_braille_letter("6", ["⠋"]) #2026/06/09
        self.append_braille_letter("7", ["⠛"]) #2026/06/09
        self.append_braille_letter("8", ["⠓"]) #2026/06/09
        self.append_braille_letter("9", ["⠊"]) #2026/06/09
        self.append_braille_letter("0", ["⠚"]) #2026/06/09
        
        self.append_braille_letter(".", ["⠲"]) #2026/06/09
        self.append_braille_letter(",", ["⠂"]) #2026/06/09
        self.append_braille_letter(";", ["⠆"]) #2026/06/09
        self.append_braille_letter(":", ["⠒"]) #2026/06/09
        self.append_braille_letter("!", ["⠖"]) #2026/06/09
        self.append_braille_letter("?", ["⠦"]) #2026/06/09
        self.append_braille_letter("\u0027", ["⠄"]) #2026/06/09 '
        self.append_braille_letter("\u0022", ["⠄", "⠶"]) #2026/06/09 "
        

        self.append_braille_letter("“", ["⠘", "⠦"]) #2026/06/09
        self.append_braille_letter("”", ["⠘", "⠴"]) #2026/06/09
        self.append_braille_letter("‘", ["⠄", "⠦"]) #2026/06/09
        self.append_braille_letter("’", ["⠄", "⠴"]) #2026/06/09
        self.append_braille_letter("(", ["⠈", "⠣"]) #2026/08/01
        self.append_braille_letter(")", ["⠈", "⠜"]) #2026/08/01
        self.append_braille_letter("[", ["⠨", "⠣"]) #2026/08/01
        self.append_braille_letter("]", ["⠨", "⠜"]) #2026/08/01
        self.append_braille_letter("{", ["⠸", "⠣"]) #2026/08/01
        self.append_braille_letter("}", ["⠸", "⠜"]) #2026/08/01

        self.append_braille_letter("\u002F", ["⠸", "⠌"]) #2026/06/09 /
        self.append_braille_letter("\u005C", ["⠸", "⠡"]) #2026/06/09 \


        #math
        self.append_braille_letter("\u0023", ["⠸", "⠹"]) #2026/06/09 #
        self.append_braille_letter("+", ["⠐", "⠖"]) #2026/06/09 
        self.append_braille_letter("−", ["⠐", "⠤"]) #2026/06/09
        self.append_braille_letter("×", ["⠐", "⠦"]) #2026/06/09
        self.append_braille_letter("*", ["⠐", "⠔"]) #2026/06/09
        self.append_braille_letter("÷", ["⠐", "⠌"]) #2026/06/09
        self.append_braille_letter("%", ["⠨", "⠴"]) #2026/06/09
        self.append_braille_letter("=", ["⠐", "⠶"]) #2026/06/09


        #money simbol
        self.append_braille_letter("$", ["⠈", "⠎"]) #2026/06/09
        self.append_braille_letter("¢", ["⠈", "⠉"]) #2026/06/09
        self.append_braille_letter("¥", ["⠈", "⠽"]) #2026/06/09
        self.append_braille_letter("€", ["⠈", "⠑"]) #2026/06/09
        self.append_braille_letter("£", ["⠈", "⠇"]) #2026/06/09
        self.append_braille_letter("₣", ["⠈", "⠋"]) #2026/06/09
        self.append_braille_letter("₦", ["⠈", "⠝"]) #2026/06/09

        #yajiru
        self.append_braille_letter("→", ["⠳", "⠕"]) #2026/06/09
        self.append_braille_letter("↓", ["⠳", "⠩"]) #2026/06/09
        self.append_braille_letter("←", ["⠳", "⠪"]) #2026/06/09
        self.append_braille_letter("↑", ["⠳", "⠬"]) #2026/06/09

        #general
        self.append_braille_letter("©", ["⠘", "⠉"]) #2026/06/09
        self.append_braille_letter("®", ["⠘", "⠗"]) #2026/06/09
        self.append_braille_letter("™", ["⠘", "⠞"]) #2026/06/09
        self.append_braille_letter("♀", ["⠘", "⠭"]) #2026/06/09
        self.append_braille_letter("♂", ["⠘", "⠽"]) #2026/06/09
        self.append_braille_letter("§", ["⠘", "⠎"]) #2026/06/09
        self.append_braille_letter("&", ["⠯"]) #2026/08/01

        #internet
        self.append_braille_letter("@", ["⠈"]) #2026/06/09

        #Greek
        self.append_braille_letter("[Α]", ["⠸", "⠁"]) #2026/08/01
        self.append_braille_letter("[Β]", ["⠸", "⠃"]) #2026/08/01
        self.append_braille_letter("[Γ]", ["⠸", "⠛"]) #2026/08/01
        self.append_braille_letter("[Δ]", ["⠸", "⠙"]) #2026/08/01
        self.append_braille_letter("[Ε]", ["⠸", "⠑"]) #2026/08/01
        self.append_braille_letter("[Ζ]", ["⠸", "⠵"]) #2026/08/01
        self.append_braille_letter("[Η]", ["⠸", "⠸"]) #2026/08/01
        self.append_braille_letter("[Θ]", ["⠸", "⠹"]) #2026/08/01
        self.append_braille_letter("[Ι]", ["⠸", "⠊"]) #2026/08/01
        self.append_braille_letter("[Κ]", ["⠸", "⠅"]) #2026/08/01
        self.append_braille_letter("[Λ]", ["⠸", "⠇"]) #2026/08/01
        self.append_braille_letter("[Μ]", ["⠸", "⠍"]) #2026/08/01
        self.append_braille_letter("[Ν]", ["⠸", "⠝"]) #2026/08/01
        self.append_braille_letter("[Ξ]", ["⠸", "⠭"]) #2026/08/01
        self.append_braille_letter("[Ο]", ["⠸", "⠕"]) #2026/08/01
        self.append_braille_letter("[Π]", ["⠸", "⠏"]) #2026/08/01
        self.append_braille_letter("[Ρ]", ["⠸", "⠗"]) #2026/08/01
        self.append_braille_letter("[Σ]", ["⠸", "⠎"]) #2026/08/01
        self.append_braille_letter("[Τ]", ["⠸", "⠞"]) #2026/08/01
        self.append_braille_letter("[Υ]", ["⠸", "⠥"]) #2026/08/01
        self.append_braille_letter("[Φ]", ["⠸", "⠋"]) #2026/08/01
        self.append_braille_letter("[Χ]", ["⠸", "⠯"]) #2026/08/01
        self.append_braille_letter("[Ψ]", ["⠸", "⠽"]) #2026/08/01
        self.append_braille_letter("[Ω]", ["⠸", "⠺"]) #2026/08/01

        self.append_braille_letter("[α]", ["⠰", "⠁"]) #2026/08/01
        self.append_braille_letter("[β]", ["⠰", "⠃"]) #2026/08/01
        self.append_braille_letter("[γ]", ["⠰", "⠛"]) #2026/08/01
        self.append_braille_letter("[δ]", ["⠰", "⠙"]) #2026/08/01
        self.append_braille_letter("[ε]", ["⠰", "⠑"]) #2026/08/01
        self.append_braille_letter("[ζ]", ["⠰", "⠵"]) #2026/08/01
        self.append_braille_letter("[η]", ["⠰", "⠸"]) #2026/08/01
        self.append_braille_letter("[θ]", ["⠰", "⠹"]) #2026/08/01
        self.append_braille_letter("[ι]", ["⠰", "⠊"]) #2026/08/01
        self.append_braille_letter("[κ]", ["⠰", "⠅"]) #2026/08/01
        self.append_braille_letter("[λ]", ["⠰", "⠇"]) #2026/08/01
        self.append_braille_letter("[μ]", ["⠰", "⠍"]) #2026/08/01
        self.append_braille_letter("[ν]", ["⠰", "⠝"]) #2026/08/01
        self.append_braille_letter("[ξ]", ["⠰", "⠭"]) #2026/08/01
        self.append_braille_letter("[ο]", ["⠰", "⠕"]) #2026/08/01
        self.append_braille_letter("[π]", ["⠰", "⠏"]) #2026/08/01
        self.append_braille_letter("[ρ]", ["⠰", "⠗"]) #2026/08/01
        self.append_braille_letter("[σ]", ["⠰", "⠎"]) #2026/08/01
        self.append_braille_letter("[τ]", ["⠰", "⠞"]) #2026/08/01
        self.append_braille_letter("[υ]", ["⠰", "⠥"]) #2026/08/01
        self.append_braille_letter("[φ]", ["⠰", "⠋"]) #2026/08/01
        self.append_braille_letter("[χ]", ["⠰", "⠯"]) #2026/08/01
        self.append_braille_letter("[ψ]", ["⠰", "⠽"]) #2026/08/01
        self.append_braille_letter("[ω]", ["⠰", "⠺"]) #2026/08/01
        self.append_braille_letter("[ς]", ["⠰", "⠎"]) #2026/08/01
