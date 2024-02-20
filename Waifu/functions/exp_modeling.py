import random
from Waifu import cusr, DB

cusr.execute("""
    CREATE TABLE IF NOT EXISTS exp_model (
        id SERIAL PRIMARY KEY,
        user_id VARCHAR(255) NOT NULL,
        exp VARCHAR(255) NOT NULL,
        rank TEXT NOT NULL
    )
""")
DB.commit()

class WaifuClient:
    level_thresholds = {
        "S Class": 1000,
        "A Class": 750,
        "B Class": 500,
        "C Class": 250,
        "D Class": 100,
        "E Class": 0
    }
    
    celestial_fragments_rewards = {
        "S Class": 10,
        "A Class": 8,
        "B Class": 6,
        "C Class": 4,
        "D Class": 2,
        "E Class": 0
    }

    def __init__(self, user_id):
        self.user_id = user_id

    async def handle_waifu_catch(self):
        exp_gained = random.randint(99, 200)
        await self.update_experience(exp_gained)

    async def update_experience(self, exp_gained):
        current_exp_model = await fetch_model(self.user_id)
        current_exp = int(current_exp_model[2]) if current_exp_model else 0
        new_exp = current_exp + exp_gained
        new_rank = self.calculate_rank(new_exp)
        
        if current_exp_model:
            cusr.execute("""
                UPDATE exp_model
                SET exp = %s, rank = %s
                WHERE user_id = %s
            """, (str(new_exp), new_rank, str(self.user_id)))
        else:
            cusr.execute("""
                INSERT INTO exp_model (user_id, exp, rank)
                VALUES (%s, %s, %s)
            """, (str(self.user_id), str(new_exp), new_rank))
        
        DB.commit()

    def calculate_rank(self, exp):
        for rank, threshold in self.level_thresholds.items():
            if exp >= threshold:
                return rank
        return "E Class"

async def fetch_model(user_id):
    cusr.execute("SELECT * FROM exp_model WHERE user_id = %s", (str(user_id),))
    result = cusr.fetchone()
    return result
    
