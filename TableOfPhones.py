class TableOfPhones:
    num_of_specs = 29
    num_of_phones = 9000

    table = []  # each row is criteria, each column is phone
    criteria_weight = []
    candidate_dict = {}
    specs_dict = {
                    0: "battery",
                    1: "year",
                    2: "height",
                    3: "width",
                    4: "weight",
                    5: "numofsim",
                    6: "simtype",
                    7: "displaysize",
                    8: "displayresolution",
                    9: "os",
                    10: "cpu",
                    11: "memoryslot",
                    12: "maxextmemory",
                    13: "RAM",
                    14: "cam1MP",
                    15: "cam1video",
                    16: "cam2MP",
                    17: "cam2video",
                    18: "ir",
                    19: "radio",
                    20: "usb",
                    21: "nfc",
                    22: "fingerprint",
                    23: "price",
                    24: "basemark",
                    25: "loudspeaker",
                    26: "audioquality",
                    27: "endurance",
                    28: "waterproof"
    }

    def __init__(self, db, target):
        i = 0
        for brand in db:
            for model in db[brand]["models"]:
                self.candidate_dict[i] = {"brand": brand, "model": model}
                i += 1
        if target == "kids":
            self.criteria_weight = [5,4,3,3,4,1,1,5,5,5,4,2,4,4,4,4,4,4,2,1,1,1,2,5,3,5,5,5,4]
            self.build_table(db, "kids")
        elif target == "hightech":
            self.criteria_weight = [5,5,3,3,4,4,3,4,5,4,4,5,5,5,5,5,5,5,2,1,3,3,4,5,4,1,2,5,4]
            self.build_table(db, "hightech")
        elif target == "pensioners":
            self.criteria_weight = [5,2,4,4,4,1,1,5,3,1,1,5,5,1,4,4,4,4,4,5,4,2,1,5,1,5,5,5,3]
            self.build_table(db, "pensioners")

    def build_table(self, db, target):
        for i in range(0, self.num_of_specs):
            criteria = []
            for j in range(0, self.num_of_phones):
                spec_value = db[self.candidate_dict[j]["brand"]]["models"][self.candidate_dict[j]["model"]]["specs"][self.specs_dict[i]]
                criteria.append(self.spec_grade(self.specs_dict[i], spec_value, target))
            self.table.append(criteria)
        
    def spec_grade(self, spec, spec_value, target):
        
