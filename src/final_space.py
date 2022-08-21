from requests import get


class FinalSpace:
	def __init__(self):
		self.api = "https://finalspaceapi.com/api/v0"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
			"accept": "application/json"
		}
	
	def get_endpoints(self):
		return get(
			f"{self.api}/", headers=self.headers).json()
	
	def get_character(self, character_id: int):
		return get(
			f"{self.api}/character/{character_id}",
			headers=self.headers).json()
			
	def get_all_characters(self):
		return get(
			f"{self.api}/character",
			headers=self.headers).json()
	
	def get_episode(self, episode_id: int):
		return get(
			f"{self.api}/episode/{episode_id}",
			headers=self.headers).json()
			
	def get_all_episodes(self):
		return get(
			f"{self.api}/episode",
			headers=self.headers).json()
	
	def get_location(self, location_id: int):
		return get(
			f"{self.api}/locations/{location_id}",
			headers=self.headers).json()
			
	def get_all_locations(self):
		return get(
			f"{self.api}/locations",
			headers=self.headers).json()
	
	def get_all_quotes(self):
		return get(
			f"{self.api}/quote",
			headers=self.headers).json()
