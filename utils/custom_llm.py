from litellm import completion
from langchain.llms.base import LLM
from typing import Any, List, Mapping, Optional

class CustomLLM(LLM):
    model_name: str = "groq/llama3-70b-8192"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        response = completion(model=self.model_name, messages=[{"role": "user", "content": prompt}])
        return response.choices[0].message.content

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"model_name": self.model_name}

    @property
    def _llm_type(self) -> str:
        return "custom"