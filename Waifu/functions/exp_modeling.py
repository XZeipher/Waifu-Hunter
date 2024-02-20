from Waifu import cusr, DB

class WaifuClient:
    level_thresholds = {
        "S Class": 10000,
        "A Class": 5000,
        "B Class": 1000,
        "C Class": 500,
        "D Class": 200,
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
        
        if new_rank != current_exp_model[3]:  # Check if the rank has changed (level up)
            celestial_fragments_reward = self.celestial_fragments_rewards.get(new_rank, 0)
            self.reward_celestial_fragments(celestial_fragments_reward)
        
        DB.commit()

    def calculate_rank(self, exp):
        for rank, threshold in self.level_thresholds.items():
            if exp >= threshold:
                return rank
        return "E Class"

    def reward_celestial_fragments(self, fragments):
        # Implement your logic to reward celestial fragments to the user
        pass

async def fetch_model(user_id):
    cusr.execute("SELECT * FROM exp_model WHERE user_id = %s", (str(user_id),))
    result = cusr.fetchone()
    return result
    
