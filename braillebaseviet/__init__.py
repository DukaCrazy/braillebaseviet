from braillebase import *

class BrailleBaseViet(BrailleBase):
    def __init__(self):

        """
        """
        super().__init__()
        self.setting_braille_rules_uppercase("⠠", "⠠⠠") #2026/05/18
        #Viet
        self.append_braille_letter("ă", ["⠜"]) #2026/08/01
        self.append_braille_letter("â", ["⠡"]) #2026/08/01
        self.append_braille_letter("ê", ["⠣"]) #2026/08/01
        self.append_braille_letter("ô", ["⠹"]) #2026/08/01
        self.append_braille_letter("ơ", ["⠪"]) #2026/08/01
        self.append_braille_letter("ư", ["⠳"]) #2026/08/01

        self.append_braille_letter("á", ["⠔","⠁"]) #2026/08/01
        self.append_braille_letter("ắ", ["⠔","⠜"]) #2026/08/01
        self.append_braille_letter("ấ", ["⠔","⠡"]) #2026/08/01
        self.append_braille_letter("à", ["⠰","⠁"]) #2026/08/01
        self.append_braille_letter("ằ", ["⠰","⠜"]) #2026/08/01
        self.append_braille_letter("ầ", ["⠰","⠡"]) #2026/08/01
        self.append_braille_letter("ả", ["⠢","⠁"]) #2026/08/01
        self.append_braille_letter("ẳ", ["⠢","⠜"]) #2026/08/01
        self.append_braille_letter("ẩ", ["⠢","⠡"]) #2026/08/01
        self.append_braille_letter("ã", ["⠤","⠁"]) #2026/08/01
        self.append_braille_letter("ẵ", ["⠤","⠜"]) #2026/08/01
        self.append_braille_letter("ẫ", ["⠤","⠡"]) #2026/08/01
        self.append_braille_letter("ạ", ["⠠","⠁"]) #2026/08/01
        self.append_braille_letter("ặ", ["⠠","⠜"]) #2026/08/01
        self.append_braille_letter("ậ", ["⠠","⠡"]) #2026/08/01

        self.append_braille_letter("đ", ["⠮"]) #2026/08/01

        self.append_braille_letter("é", ["⠔","⠑"]) #2026/08/01
        self.append_braille_letter("ế", ["⠔","⠣"]) #2026/08/01
        self.append_braille_letter("è", ["⠰","⠑"]) #2026/08/01
        self.append_braille_letter("ề", ["⠰","⠣"]) #2026/08/01
        self.append_braille_letter("ẻ", ["⠢","⠑"]) #2026/08/01
        self.append_braille_letter("ể", ["⠢","⠣"]) #2026/08/01
        self.append_braille_letter("ẽ", ["⠤","⠑"]) #2026/08/01
        self.append_braille_letter("ễ", ["⠤","⠣"]) #2026/08/01
        self.append_braille_letter("ẹ", ["⠠","⠑"]) #2026/08/01
        self.append_braille_letter("ệ", ["⠠","⠣"]) #2026/08/01

        self.append_braille_letter("í", ["⠔","⠊"]) #2026/08/01
        self.append_braille_letter("ì", ["⠰","⠊"]) #2026/08/01
        self.append_braille_letter("ỉ", ["⠢","⠊"]) #2026/08/01
        self.append_braille_letter("ĩ", ["⠤","⠊"]) #2026/08/01
        self.append_braille_letter("ị", ["⠠","⠊"]) #2026/08/01

        self.append_braille_letter("ó", ["⠔","⠕"]) #2026/08/01
        self.append_braille_letter("ố", ["⠔","⠹"]) #2026/08/01
        self.append_braille_letter("ớ", ["⠔","⠪"]) #2026/08/01
        self.append_braille_letter("ò", ["⠰","⠕"]) #2026/08/01
        self.append_braille_letter("ồ", ["⠰","⠹"]) #2026/08/01
        self.append_braille_letter("ờ", ["⠰","⠪"]) #2026/08/01
        self.append_braille_letter("ỏ", ["⠢","⠕"]) #2026/08/01
        self.append_braille_letter("ổ", ["⠢","⠹"]) #2026/08/01
        self.append_braille_letter("ở", ["⠢","⠪"]) #2026/08/01
        self.append_braille_letter("õ", ["⠤","⠕"]) #2026/08/01
        self.append_braille_letter("ỗ", ["⠤","⠹"]) #2026/08/01
        self.append_braille_letter("ỡ", ["⠤","⠪"]) #2026/08/01
        self.append_braille_letter("ọ", ["⠠","⠕"]) #2026/08/01
        self.append_braille_letter("ộ", ["⠠","⠹"]) #2026/08/01
        self.append_braille_letter("ợ", ["⠠","⠪"]) #2026/08/01

        self.append_braille_letter("ú", ["⠔","⠥"]) #2026/08/01
        self.append_braille_letter("ứ", ["⠔","⠳"]) #2026/08/01
        self.append_braille_letter("ù", ["⠰","⠥"]) #2026/08/01
        self.append_braille_letter("ừ", ["⠰","⠳"]) #2026/08/01
        self.append_braille_letter("ủ", ["⠢","⠥"]) #2026/08/01
        self.append_braille_letter("ử", ["⠢","⠳"]) #2026/08/01
        self.append_braille_letter("ũ", ["⠤","⠥"]) #2026/08/01
        self.append_braille_letter("ữ", ["⠤","⠳"]) #2026/08/01
        self.append_braille_letter("ụ", ["⠠","⠥"]) #2026/08/01
        self.append_braille_letter("ự", ["⠠","⠳"]) #2026/08/01

        self.append_braille_letter("ý", ["⠔","⠽"]) #2026/08/01
        self.append_braille_letter("ỳ", ["⠰","⠽"]) #2026/08/01
        self.append_braille_letter("ỷ", ["⠢","⠽"]) #2026/08/01
        self.append_braille_letter("ỹ", ["⠤","⠽"]) #2026/08/01
        self.append_braille_letter("ỵ", ["⠠","⠽"]) #2026/08/01

        #Viet
        self.append_braille_letter("Â", ["⠡"], 1) #2026/08/01
        self.append_braille_letter("Ê", ["⠣"], 1) #2026/08/01
        self.append_braille_letter("Ô", ["⠹"], 1) #2026/08/01
        self.append_braille_letter("Ơ", ["⠪"], 1) #2026/08/01
        self.append_braille_letter("Ư", ["⠳"], 1) #2026/08/01

        self.append_braille_letter("Á", ["⠔","⠁"], 1) #2026/08/01
        self.append_braille_letter("Ắ", ["⠔","⠜"], 1) #2026/08/01
        self.append_braille_letter("Ấ", ["⠔","⠡"], 1) #2026/08/01
        self.append_braille_letter("À", ["⠰","⠁"], 1) #2026/08/01
        self.append_braille_letter("Ằ", ["⠰","⠜"], 1) #2026/08/01
        self.append_braille_letter("Ầ", ["⠰","⠡"], 1) #2026/08/01
        self.append_braille_letter("Ả", ["⠢","⠁"], 1) #2026/08/01
        self.append_braille_letter("Ẳ", ["⠢","⠜"], 1) #2026/08/01
        self.append_braille_letter("Ẩ", ["⠢","⠡"], 1) #2026/08/01
        self.append_braille_letter("Ã", ["⠤","⠁"], 1) #2026/08/01
        self.append_braille_letter("Ẵ", ["⠤","⠜"], 1) #2026/08/01
        self.append_braille_letter("Ẫ", ["⠤","⠡"], 1) #2026/08/01
        self.append_braille_letter("Ạ", ["⠠","⠁"], 1) #2026/08/01
        self.append_braille_letter("Ặ", ["⠠","⠜"], 1) #2026/08/01
        self.append_braille_letter("Ậ", ["⠠","⠡"], 1) #2026/08/01

        self.append_braille_letter("Đ", ["⠮"], 1) #2026/08/01

        self.append_braille_letter("É", ["⠔","⠑"], 1) #2026/08/01
        self.append_braille_letter("Ế", ["⠔","⠣"], 1) #2026/08/01
        self.append_braille_letter("È", ["⠰","⠑"], 1) #2026/08/01
        self.append_braille_letter("Ề", ["⠰","⠣"], 1) #2026/08/01
        self.append_braille_letter("Ẻ", ["⠢","⠑"], 1) #2026/08/01
        self.append_braille_letter("Ể", ["⠢","⠣"], 1) #2026/08/01
        self.append_braille_letter("Ẽ", ["⠤","⠑"], 1) #2026/08/01
        self.append_braille_letter("Ễ", ["⠤","⠣"], 1) #2026/08/01
        self.append_braille_letter("Ẹ", ["⠠","⠑"], 1) #2026/08/01
        self.append_braille_letter("Ệ", ["⠠","⠣"], 1) #2026/08/01

        self.append_braille_letter("Í", ["⠔","⠊"], 1) #2026/08/01
        self.append_braille_letter("Ì", ["⠰","⠊"], 1) #2026/08/01
        self.append_braille_letter("Ỉ", ["⠢","⠊"], 1) #2026/08/01
        self.append_braille_letter("Ĩ", ["⠤","⠊"], 1) #2026/08/01
        self.append_braille_letter("Ị", ["⠠","⠊"], 1) #2026/08/01

        self.append_braille_letter("Ó", ["⠔","⠕"], 1) #2026/08/01
        self.append_braille_letter("Ố", ["⠔","⠹"], 1) #2026/08/01
        self.append_braille_letter("Ớ", ["⠔","⠪"], 1) #2026/08/01
        self.append_braille_letter("Ò", ["⠰","⠕"], 1) #2026/08/01
        self.append_braille_letter("Ồ", ["⠰","⠹"], 1) #2026/08/01
        self.append_braille_letter("Ờ", ["⠰","⠪"], 1) #2026/08/01
        self.append_braille_letter("Ỏ", ["⠢","⠕"], 1) #2026/08/01
        self.append_braille_letter("Ổ", ["⠢","⠹"], 1) #2026/08/01
        self.append_braille_letter("Ở", ["⠢","⠪"], 1) #2026/08/01
        self.append_braille_letter("Õ", ["⠤","⠕"], 1) #2026/08/01
        self.append_braille_letter("Ỗ", ["⠤","⠹"], 1) #2026/08/01
        self.append_braille_letter("Ỡ", ["⠤","⠪"], 1) #2026/08/01
        self.append_braille_letter("Ọ", ["⠠","⠕"], 1) #2026/08/01
        self.append_braille_letter("Ộ", ["⠠","⠹"], 1) #2026/08/01
        self.append_braille_letter("Ợ", ["⠠","⠪"], 1) #2026/08/01

        self.append_braille_letter("Ú", ["⠔","⠥"], 1) #2026/08/01
        self.append_braille_letter("Ứ", ["⠔","⠳"], 1) #2026/08/01
        self.append_braille_letter("Ù", ["⠰","⠥"], 1) #2026/08/01
        self.append_braille_letter("Ừ", ["⠰","⠳"], 1) #2026/08/01
        self.append_braille_letter("Ủ", ["⠢","⠥"], 1) #2026/08/01
        self.append_braille_letter("Ử", ["⠢","⠳"], 1) #2026/08/01
        self.append_braille_letter("Ũ", ["⠤","⠥"], 1) #2026/08/01
        self.append_braille_letter("Ữ", ["⠤","⠳"], 1) #2026/08/01
        self.append_braille_letter("Ụ", ["⠠","⠥"], 1) #2026/08/01
        self.append_braille_letter("Ự", ["⠠","⠳"], 1) #2026/08/01

        self.append_braille_letter("Ý", ["⠔","⠽"], 1) #2026/08/01
        self.append_braille_letter("Ỳ", ["⠰","⠽"], 1) #2026/08/01
        self.append_braille_letter("Ỷ", ["⠢","⠽"], 1) #2026/08/01
        self.append_braille_letter("Ỹ", ["⠤","⠽"], 1) #2026/08/01
        self.append_braille_letter("Ỵ", ["⠠","⠽"], 1) #2026/08/01

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
        self.append_braille_letter("[‘]", ["⠄"]) #2026/08/02 apostrophe 
        self.append_braille_letter("[´]", ["⠄"]) #2026/08/02 apostrophe 
        self.append_braille_letter("[*]", ["⠐", "⠔"]) #2026/08/02 asterisk 
        self.append_braille_letter("[—]", ["⠐","⠠", "⠤"]) #2026/08/02 longdash
        self.append_braille_letter("[-]", ["⠠", "⠤"]) #2026/08/02 dash
        self.append_braille_letter("-", ["⠠", "⠤"]) #2026/08/02 dash
        
        #internet
        self.append_braille_letter("@", ["⠈", "⠁"]) #2026/06/09
        self.append_braille_letter("[@]", ["⠈", "⠁"]) #2026/08/02
