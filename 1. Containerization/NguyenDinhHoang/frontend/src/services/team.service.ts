import AuthHeader from "./auth.header"
import pmServer from "src/api/pmServer"

const CreateTeam = async (teamName: string, membersId: any[]) => {
  const response = await pmServer.post(`/pm/create-team`, { teamName: teamName, membersId: membersId }, { headers: AuthHeader() })
  return response.data
}

const UpdateTeam = async (userId: string, teamId: string, team: any) => {
  const response = await pmServer.put(`pm/update-team`, { userId: userId, teamId: teamId, team: team }, { headers: AuthHeader() })
  return response.data
}

const GetTeamsByUserId = async (userId: string) => {
  const response = await pmServer.get(`/pm/get-teams-by-userid?userId=${userId}`, { headers: AuthHeader() })
  return response.data
}

const DeleteTeamByTeamId = async (userId: string, teamId: string) => {
  const response = await pmServer.post(`/pm/delete-team-by-id`, { userId: userId, teamId: teamId }, { headers: AuthHeader() })
  return response.data
}

const RemoveTeamMember = async (memberId: string, teamId: string) => {
  const response = await pmServer.post(`/pm/remove-team-members`, { memberId: memberId, teamId: teamId }, { headers: AuthHeader() })
  return response.data
}

const UpdateTeamMember = async (userId: string, teamId: string) => {
  const response = await pmServer.put(`/pm/update-team-member`, { userId: userId, teamId: teamId }, { headers: AuthHeader() })
  return response.data
}

const AddTeamMembers = async (newMembers: string[], team_id: string) => {
  const response = await pmServer.post(`/pm/add-team-members`, { newMembers: newMembers, team_id: team_id }, { headers: AuthHeader() })
  return response.data
}

const GetTeamMembers = async (teamId: string) => {
  const response = await pmServer.get(`/pm/get-teammembers-by-teamid?teamId=${teamId}`, { headers: AuthHeader() })
  return response.data
}

const PromoteTeamMember = async (memberId: string, teamId: string) => {
  const response = await pmServer.put(`/pm/promote-to-pm`, { memberId: memberId, teamId: teamId }, { headers: AuthHeader() })
  return response.data
}

const DemoteTeamMember = async (memberId: string, teamId: string) => {
  const response = await pmServer.put(`/pm/demote-to-member`, { memberId: memberId, teamId: teamId }, { headers: AuthHeader() })
  return response.data
}

const TeamsService = {
  CreateTeam,
  GetTeamsByUserId,
  DeleteTeamByTeamId,
  RemoveTeamMember,
  UpdateTeamMember,
  AddTeamMembers,
  GetTeamMembers,
  PromoteTeamMember,
  DemoteTeamMember,
  UpdateTeam
}
export default TeamsService