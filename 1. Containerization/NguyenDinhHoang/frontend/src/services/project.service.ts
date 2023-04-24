import AuthHeader from "./auth.header"
import pmServer from "src/api/pmServer"

const CreateProject = async (project: any) => {
  const response = await pmServer.post(`/pm/create-project`, project, { headers: AuthHeader() })
  return response.data
}

const DeleteProject = async (userId: string, projectId: string, teamId: string) => {
  const response = await pmServer.post(`/pm/delete-project`, { userId: userId, projectId: projectId, teamId: teamId }, { headers: AuthHeader() })
  return response.data
}

const UpdateProject = async (teamId: string, userId: string, projectId: string, project: any) => {
  const response = await pmServer.put(`/pm/update-project`, {teamId: teamId, userId:userId,projectId: projectId, project: project }, { headers: AuthHeader() })
  return response.data
}

const GetProjectByProjectId = async (projectId: string, userId: string) => {
  const response = await pmServer.get(`/pm/get-project?projectId=${projectId}&userId=${userId}`, { headers: AuthHeader() })
  return response.data
}

const CreateTaskByProjectId = async (task: any) => {
  const response = await pmServer.post(`/pm/create-task`, { task: task }, { headers: AuthHeader() })
  return response.data
}

const UpdateTaskByTaskId = async (userId: string, taskId: string, task: any) => {
  const response = await pmServer.put(`/pm/update-task`, { userId: userId, taskId: taskId, task: task }, { headers: AuthHeader() })
  return response.data
}

const GetTasksByUserId = async (userId: string) => {
  const response = await pmServer.get(`/pm/get-tasks-by-userid?userId=${userId}`, { headers: AuthHeader() })
  return response.data
}

const CreateCommentByTaskId = async (userId: string, taskId: string, content: string) => {
  const response = await pmServer.post(`/pm/create-comment`, { userId: userId, taskId: taskId, content: content }, { headers: AuthHeader() })
  return response.data
}

const DeleteTaskByTaskId = async (taskId: string) => {
  const response = await pmServer.post(`/pm/delete-task`, { taskId: taskId }, { headers: AuthHeader() })
  return response.data
}

const ProjectService = {
  CreateProject,
  DeleteProject,
  GetProjectByProjectId,
  CreateTaskByProjectId,
  UpdateTaskByTaskId,
  GetTasksByUserId,
  CreateCommentByTaskId,
  UpdateProject,
  DeleteTaskByTaskId
}
export default ProjectService