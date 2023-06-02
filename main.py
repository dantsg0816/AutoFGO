from tabnanny import check
import stage

if __name__ == '__main__':
    # skill list: [[skill_num, mate_target]] 
    # servant skills: 1~9
    # master skills: 11~13
    # mate target: 1~3
    # np list: 1~3 
    
    stg = stage.Stage()
    stg.support_servant = ''
    stg.support_craftessence = ''
    stg.party_num = 3
    stg.skill_list_1 = [[2, 2], [4, 0], [5, 2], [6, 0], [7, 2], [8, 2]]
    stg.np_list_1 = []
    stg.card_rule_1 = 'rw'
    stg.skill_list_2 = [[3, 2], [9, 2]]
    stg.np_list_2 = [2]
    stg.card_rule_2 = 'rw'
    stg.skill_list_3 = [[1, 2], [4, 0], [5, 2]]
    stg.np_list_3 = [2]
    stg.card_rule_3 = 'rw' # 'r' 'b' 'rw' 'bw'
    stg.apple = 'gold' # gold silver bronze

    stg.run()

    #stage.open_boxes()
    