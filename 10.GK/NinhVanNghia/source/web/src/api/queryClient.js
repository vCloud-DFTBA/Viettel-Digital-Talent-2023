import { QueryClient } from '@tanstack/react-query';


const queryClient = new QueryClient({
    defaultOptions: {
        queries: {
            staleTime: Infinity,
            keepPreviousData: true,
            refetchOnReconnect: false,
            refetchOnWindowFocus: false,
            retry(failureCount, error) {
                return error.response
                    && !([404, 408, 409, 429, 502, 503, 504].includes(error.response.status))
                    && (failureCount < 3)
            },
        },
    },
})


export default queryClient;
