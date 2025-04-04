from crewai_tools import BaseTool
import os
from datetime import datetime
from agentops import record_tool

class CustomFileWriterTool(BaseTool):
    name: str = "Custom File Writer Tool"
    description: str = "Write content to a file."

    @record_tool(tool_name="My own file writer tool")
    def _run(self, filename: str, content: str) -> str:
        # Remove .md extension if present
        filename = filename.removesuffix('.md')
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename}_{timestamp}.md"
        
        output_dir = 'ainews'
        os.makedirs(output_dir, exist_ok=True)

        # Combine the output directory with the filename
        file_path = os.path.join(output_dir, filename)
        
        try:
            # Write the content to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            return f"The content has been successfully written to the file: {file_path}"
        except Exception as e:
            return f"An error occurred while writing to the file: {str(e)}"
