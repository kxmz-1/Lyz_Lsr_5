import json
from pathlib import Path

class recorder(object):
    def __init__(self, source, migrate):
        self.record = []
        self.sourceapp = source
        self.migrateapp = migrate
        self.ui_hierarchy = []

    def add_event(self, event, hierarchy):
        self.record.append(event)
        self.ui_hierarchy.append(hierarchy)

    def save_file(self):
        self.remove_cyclic_events()
        p = Path("C:\\Users\\11303\\Desktop\\miaozi\\migrate\\" + self.sourceapp)
        p.mkdir(exist_ok=True)
        with open("C:\\Users\\11303\\Desktop\\miaozi\\migrate\\" + self.sourceapp + "\\" + self.sourceapp + '-' + self.migrateapp + '.json', 'w') as f:
            json.dump(self.record, f, indent=4)

    def compare_attributes(self, event1, event2):
        function_attributes = ["class", "resource-id", "text", "content-desc", "action"]
        for attr in function_attributes:
            if attr == "action":
                if json.dumps(event1[attr]) != json.dumps(event2[attr]):
                    return False
            elif event1[attr] != event2[attr]:
                return False
        return True

    def is_cycle(self, idx1, idx2):
        if self.compare_attributes(self.record[idx1], self.record[idx2]):
            return True
        if self.ui_hierarchy[idx1] == self.ui_hierarchy[idx2]:
            return True
        return False

    def remove_cyclic_events(self):
        events_to_remove = []
        for i in range(len(self.record)):
            for j in range(i + 1, len(self.record)):
                if self.is_cycle(i, j):
                    events_to_remove += list(range(i + 1, j))
                    events_to_remove.append(j)
                    break
        self.record = [event for i, event in enumerate(self.record) if i not in events_to_remove]

