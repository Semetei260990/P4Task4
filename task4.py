class ContactList(list):
    def __init__(self, lsm, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lsm = lsm
    
    def search_by_name(self, name):
        s = []
        for i in self.lsm:
            if i == name:
                s.append(i)
        print(s)

all_contacts = ContactList(['Semetei', 'Dastan', 'Gulazana', 'Iskender'])
all_contacts.search_by_name('Dastan')


