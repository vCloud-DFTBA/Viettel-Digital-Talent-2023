import axiosClient from "./axiosClient";
import { useQuery, useMutation } from "@tanstack/react-query";


const attendeeKeys = {
    list() {
        return ['attendee']
    },
    get(attendeeId) {
        return [...this.list(), attendeeId]
    },
}


const attendeeQuery = {
    useList({query, params, body, options}={}) {
        return useQuery(
            attendeeKeys.list(),
            async () => {return await axiosClient.get(`/attendee`, {params: query, ...body})},
            options,
        )
    },

    useGet({query, params, body, options}={}) {
        return useQuery(
            attendeeKeys.get(),
            async () => {return await axiosClient.get(`/attendee/${params}`, {params: query, ...body})},
            options,
        )
    },
}


export {
    attendeeKeys,
    attendeeQuery,
}
