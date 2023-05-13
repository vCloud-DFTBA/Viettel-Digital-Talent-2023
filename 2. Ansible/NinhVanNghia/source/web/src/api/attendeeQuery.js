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
            () => axiosClient.get(`/api/v1/attendee`, {params: query, ...body}),
            options,
        )
    },

    useGet({query, params, body, options}={}) {
        return useQuery(
            attendeeKeys.get(),
            axiosClient.get(`/api/v1/attendee/${params}`, {params: query, ...body}),
            options,
        )
    },


    // usePurchaseMutation(options) {
    //     return useMutation({
    //         mutationKey: attendeeKeys.list(),
    //         mutationFn(ordererInfo) {
    //             const orderItems = queryClient.getQueryData(attendeeKeys.list())
    //                 .filter(item => item.check)
    //                 .map(({type, id, amount}) => ({type, id, amount}))

    //             return axiosClient.post('/make-order', {...ordererInfo, orderItems})
    //         },
    //         cacheTime: 0,
    //         onSuccess() {
    //             queryClient.setQueryData(attendeeKeys.list(), (data) => data.filter(item => !item.check))
    //             ToastHelper.showSuccess('Đặt hàng thành công')
    //         },
    //         onError(error) {
    //             if (error.response.status === 404)
    //                 queryClient.setQueryData(attendeeKeys.list(), (data) => data.filter(item => !item.check))
    //         },
    //         ...options,
    //     })
    // },
}


export {
    attendeeKeys,
    attendeeQuery,
}
